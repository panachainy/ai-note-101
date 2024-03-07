from langchain.chains import create_retrieval_chain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import getpass
import os
from langchain_community.vectorstores import Chroma
from langchain_google_genai import HarmBlockThreshold, HarmCategory
from langchain.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain import hub
from langchain_community.document_loaders import PyPDFLoader
from typing import (
    List,
)

from dotenv import load_dotenv
load_dotenv()

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass("Provide your Google API key here")

config = {
    **os.environ,  # override loaded values with environment variables
}
resource_dir = "./resources"
api_key = config["GOOGLE_API_KEY"]

# ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0,
    top_p=0.85,
    google_api_key=api_key,
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
    # FIXME: not sure
    convert_system_message_to_human=True
)


def ex_chat(question: str):
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)

    chain = prompt | llm

    print(chain.invoke({"question": question}))

# ex_chat("How much is 2+2?")


def load_pdf_single_file(path: str):
    loader = PyPDFLoader(path)
    pages = loader.load()

    print(len(pages))
    print(pages[0].page_content[0:500])

    print(pages[0].metadata)
    return pages


# load_pdf_single_file('resources/ex-eng.pdf')

print('=====================================================================')


def multiple_pdf_load(paths: list[str]):
    # Load PDFs
    loaders = []
    for path in paths:
        loaders.append(PyPDFLoader(path))

    docs = []
    for loader in loaders:
        docs.extend(loader.load())

    return docs


def load_docs_to_splitter(docs: list) -> List[Document]:
    # Define the Text Splitter
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=150
    )

    # Create a split of the document using the text splitter
    splits = text_splitter.split_documents(docs)
    return splits


def get_files_from_directory(directory: str) -> List[str]:
    files = []
    for file in os.listdir(directory):
        if file.endswith(".pdf"):
            file_path = "/".join([directory, file])
            files.append(file_path)
    return files


def get_vectordb() -> any:
    persist_directory = 'docs/chroma/'
    embedding = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key,
        task_type="retrieval_query"
    )
    # check if have chroma in local need to skip `Chroma.from_documents` use `Chroma` instead
    if os.path.exists(persist_directory+'chroma.sqlite3'):
        print('=== retrieve old Chroma ===')
        return Chroma(
            persist_directory=persist_directory,
            embedding_function=embedding,
        )
    else:
        print('=== new Chroma ===')
        files_path = get_files_from_directory(resource_dir)
        docs = multiple_pdf_load(files_path)
        splits = load_docs_to_splitter(docs)
        return Chroma.from_documents(
            documents=splits,
            embedding=embedding,
            persist_directory=persist_directory
        )


vectordb = get_vectordb()

print(vectordb._collection.count())
print(vectordb._collection)

retriever = vectordb.as_retriever()

retrieval_qa_chat_prompt = hub.pull("langchain-ai/retrieval-qa-chat")

combine_docs_chain = create_stuff_documents_chain(
    llm, retrieval_qa_chat_prompt
)

retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

input = "how to cook omelette?"
result = retrieval_chain.invoke({"input": input})
print(result)
