import os
import sys
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

config = {
    **os.environ,  # override loaded values with environment variables
}

api_key = config["GOOGLE_API_KEY"]

llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=api_key)


template = """Question: {question}

Answer: Let's think step by step."""
prompt = PromptTemplate.from_template(template)

chain = prompt | llm

question = "How much is 2+2?"
print(chain.invoke({"question": question}))


# print(
#     llm.invoke(
#         "Hi"
#     )
# )


# for chunk in chain.stream({"question": question}):
#     sys.stdout.write(chunk)
#     sys.stdout.flush()
