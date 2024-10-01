import os
import json
import sys
import boto3
import streamlit as st

from langchain_aws import BedrockLLM, BedrockEmbeddings

from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA    

from langchain_community.vectorstores import FAISS

from QASystem.ingestion import data_ingestion, get_vector_store
from QASystem.retrievalandgeneration import get_llama3_llm, get_response_llm

# Initialize Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock)

def main():
    # Page configuration
    st.set_page_config(page_title="Document Q&A Assistant", page_icon="📚", layout="wide")
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("📚 Document Q&A Assistant")
        st.markdown("Ask questions about your PDF documents using AI-powered analysis.")
        
        user_question = st.text_input("What would you like to know?", placeholder="Enter your question here...")
        
        if st.button("Get Answer", key="get_answer"):
            if user_question:
                with st.spinner("Thinking..."):
                    try:
                        faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
                        llm = get_llama3_llm()
                        response = get_response_llm(llm, faiss_index, user_question)
                        st.success("Here's what I found:")
                        st.write(response)
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")
            else:
                st.warning("Please enter a question.")
    
    # Sidebar
    with col2:
        st.sidebar.title("📊 Vector Store Management")
        
        if st.sidebar.button("Update Vector Store", key="update_vectors"):
            with st.sidebar.spinner("Processing documents..."):
                try:
                    docs = data_ingestion()
                    get_vector_store(docs)
                    st.sidebar.success("Vector store updated successfully!")
                except Exception as e:
                    st.sidebar.error(f"An error occurred: {str(e)}")
        
        st.sidebar.markdown("---")
        st.sidebar.info(
            "This app uses LangChain and AWS Bedrock to provide intelligent "
            "answers to your questions about the uploaded PDF documents."
        )

if __name__ == "__main__":
    main()









