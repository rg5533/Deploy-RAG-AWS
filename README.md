# Document Q&A Assistant

## Overview

The Document Q&A Assistant is an AI-powered application that allows users to ask questions about PDF documents. It uses LangChain and AWS Bedrock to provide intelligent answers based on the content of the uploaded documents.

## Features

- Upload and process PDF documents
- Ask questions about the content of the documents
- AI-powered analysis and response generation
- Vector store management for efficient document retrieval

## Technology Stack

- Python
- Streamlit
- LangChain
- AWS Bedrock
- FAISS (Facebook AI Similarity Search)
- Docker

## Setup and Installation

1. Clone the repository
2. Install the required dependencies:
   ```pip install -e .```
3. Set up your AWS credentials and configure the Bedrock client

## Usage

1. Run the Streamlit app:
   ```streamlit run app.py```
2. Upload PDF documents using the sidebar
3. Ask questions in the main interface
4. Receive AI-generated answers based on the document content

## Project Structure

- `app.py`: Main Streamlit application
- `QASystem/`: Package containing core functionality
  - `ingestion.py`: Handles document ingestion and vector store creation
  - `retrievalandgeneration.py`: Manages retrieval and response generation
- `setup.py`: Package setup file
- `.github/workflows/main.yaml`: GitHub Actions workflow for CI/CD

## Continuous Integration and Deployment (CI/CD)

This project uses GitHub Actions for CI/CD. The workflow is defined in:

```yaml:.github/workflows/main.yaml
startLine: 1
endLine: 56
```

The CI/CD workflow performs the following steps:
1. Runs linting and unit tests
2. Builds a Docker image
3. Pushes the image to Amazon Elastic Container Registry (ECR)

## Deployment Options

The Docker image pushed to ECR can be easily deployed using various AWS services:

1. **AWS App Runner**: For a fully managed, serverless deployment
2. **Amazon SageMaker**: For machine learning model deployment and serving

To deploy using these services, configure them to pull the latest image from your ECR repository.

## License

[Specify your license here]
