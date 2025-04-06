import os
from pinecone import Pinecone
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from app.chat.embeddings.openai import embeddings
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Pinecone instance
pc = Pinecone(
    api_key=os.getenv("PINECONE_API_KEY")
)

# Get index name
index_name = os.getenv("PINECONE_INDEX_NAME", "")


# Create vector store
vector_store = LangchainPinecone.from_existing_index(
    index_name=index_name,
    embedding=embeddings,
)

def build_retriever(chat_args):
    search_kwargs = {"filter":{"pdf_id":chat_args.pdf_id }}
    return vector_store.as_retriever(search_kwargs=search_kwargs)