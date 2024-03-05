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

def ex_chat():
    template = """Question: {question}

    Answer: Let's think step by step."""
    prompt = PromptTemplate.from_template(template)

    chain = prompt | llm

    question = "How much is 2+2?"
    print(chain.invoke({"question": question}))


def load_pdf_single_file(path):
    from langchain.document_loaders import PyPDFLoader
    loader = PyPDFLoader(path)
    pages = loader.load()

    print(len(pages))
    print(pages[0].page_content[0:500])

    print(pages[0].metadata)
    return pages

load_pdf_single_file('resources/Legal-AI-a-beginners-guide-web.pdf')

# loaders = [
#     # Duplicate documents on purpose - messy data
#     PyPDFLoader("resources/Legal-AI-a-beginners-guide-web.pdf"),
#     # PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture01.pdf"),
#     # PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture02.pdf"),
#     # PyPDFLoader("docs/cs229_lectures/MachineLearning-Lecture03.pdf")
# ]
# docs = []
# for loader in loaders:
#     docs.extend(loader.load())


#Load the document by calling loader.load()

# {'source': 'docs/cs229_lectures/MachineLearning-Lecture01.pdf', 'page': 0}

# print(
#     llm.invoke(
#         "Hi"
#     )
# )


# for chunk in chain.stream({"question": question}):
#     sys.stdout.write(chunk)
#     sys.stdout.flush()
