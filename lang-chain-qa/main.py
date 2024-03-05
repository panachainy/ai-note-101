from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
import os
import sys
from langchain_google_genai import GoogleGenerativeAI, HarmBlockThreshold, HarmCategory
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

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


docs = multiple_pdf_load(
    ['resources/ex-eng.pdf', 'resources/ex-thai.pdf']
)


def load_docs_to_splitter(docs: list):
    # Define the Text Splitter
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=150
    )

    # Create a split of the document using the text splitter
    splits = text_splitter.split_documents(docs)

# load_docs_to_splitter(docs)

# embedding = OpenAIEmbeddings()
