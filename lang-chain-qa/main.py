from langchain_google_genai import GoogleGenerativeAIEmbeddings
import getpass
import os
from langchain_community.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
import sys
from langchain_google_genai import GoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain.prompts import PromptTemplate
from langchain_core.documents import Document
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

api_key = config["GOOGLE_API_KEY"]

# llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key,
#                          safety_settings={
#                              HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
#                          },
#                          )

llm = GoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=api_key,
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
)


def ex_chat(question: str):
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)

    chain = prompt | llm

    print(chain.invoke({"question": question}))

# ex_chat("How much is 2+2?")


def load_pdf_single_file(path: str):
    from langchain.document_loaders import PyPDFLoader
    loader = PyPDFLoader(path)
    pages = loader.load()

    print(len(pages))
    print(pages[0].page_content[0:500])

    print(pages[0].metadata)
    return pages


# load_pdf_single_file('resources/ex-eng.pdf')

print('=====================================================================')


def multiple_pdf_load(paths: list[str]):
    from langchain.document_loaders import PyPDFLoader

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


def get_vectordb() -> any:
    embedding = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=api_key,
        # task_type="retrieval_query",
        # task_type="retrieval_document"
    )

    persist_directory = 'docs/chroma/'

    # check if have chroma in local need to skip `Chroma.from_documents` use `Chroma` instead
    if os.path.exists(persist_directory+'chroma.sqlite3'):
        return Chroma(
            persist_directory=persist_directory
        )
    else:
        docs = multiple_pdf_load(
            ['resources/ex-eng.pdf', 'resources/ex-thai.pdf']
        )
        splits = load_docs_to_splitter(docs)
        return Chroma.from_documents(
            documents=splits,
            embedding=embedding,
            persist_directory=persist_directory
        )


# Create the vector store (only first time)
# vectordb = Chroma.from_documents(
#     documents=splits,
#     embedding=embedding,
#     persist_directory=persist_directory
# )
# vectordb = Chroma(
#     persist_directory=persist_directory,
#     embedding_function=embedding
# )

vectordb = get_vectordb()

print(vectordb._collection.count())
