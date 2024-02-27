# from langchain.chains import RetrievalQA
# from langchain.indexes import VectorstoreIndexCreator
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFLoader
from langchain_community.llms import GPT4All
from langchain.chains.question_answering import load_qa_chain

loader = PyPDFLoader("materials/eng-example.pdf")
documents = loader.load()

# print(documents)

### For multiple documents
# loaders = [....]
# documents = []
# for loader in loaders:
#     documents.extend(loader.load())

llm = GPT4All(model="./models/mistral-7b-openorca.Q4_0.gguf", n_threads=8)

chain = load_qa_chain(llm=llm, chain_type="map_reduce")
query = "what is the total number of AI publications?"
# chain.run(input_documents=documents, question=query)
