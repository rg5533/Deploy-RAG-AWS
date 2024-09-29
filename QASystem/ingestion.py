from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_aws import BedrockEmbeddings
from langchain_community.llms import Bedrock

import os
import json
import sys
import boto3


##bedrock client
bedrock=boto3.client(service_name="bedrock-runtime")
bedrock_embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock,)


def data_ingestion():
    loader=PyPDFDirectoryLoader("./data")
    documents=loader.load()
    

    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=500)
    docs=text_splitter.split_documents(documents)
    
    return docs

def get_vector_store(docs):
    vector_store_faiss = FAISS.from_documents(docs, BedrockEmbeddings())
    vector_store_faiss.save_local("faiss_index")
    
    return vector_store_faiss
    
if __name__=="__main__":
    
    docs=data_ingestion()
    get_vector_store(docs)




