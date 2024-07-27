## Data Ingestion
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai
from langchain_community.document_loaders import TextLoader
loader=TextLoader("diary.txt")
text_documents=loader.load()


import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter=RecursiveCharacterTextSplitter(chunk_size=100,chunk_overlap=20)
documents=text_splitter.split_documents(text_documents)

llm = ChatGoogleGenerativeAI(model="gemini-pro")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
## Vector Embedding And Vector Store
# from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import Chroma
db = Chroma.from_documents(documents,embeddings)

query = "Who are the authors of attention is all you need?"
retireved_results=db.similarity_search(query)
print(retireved_results[0].page_content)

# from langchain_community.llms import Ollama
# llm=Ollama(model="llama2")

# ## Design ChatPrompt Template
# from langchain_core.prompts import ChatPromptTemplate
# prompt = ChatPromptTemplate.from_template("""
# Answer the following question based only on the provided context. 
# Think step by step before providing a detailed answer. 
# I will tip you $1000 if the user finds the answer helpful. 
# <context>
# {context}
# </context>
# Question: {input}""")

# ## Chain Introduction
# ## Create Stuff Docment Chain

# from langchain.chains.combine_documents import create_stuff_documents_chain

# document_chain=create_stuff_documents_chain(llm,prompt)


# retriever=db.as_retriever()

# from langchain.chains import create_retrieval_chain
# retrieval_chain=create_retrieval_chain(retriever,document_chain)

# response=retrieval_chain.invoke({"input":"Scaled Dot-Product Attention"})

# print(response['answer'])