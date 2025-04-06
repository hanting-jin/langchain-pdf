import chunk
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.chat.vector_stores.pinecone import vector_store
# from langchain_community.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import Chroma 

"""
Generate and store embeddings for the given pdf

1. Extract text from the specified PDF.
2. Divide the extracted text into manageable chunks.
3. Generate an embedding for each chunk.
4. Persist the generated embeddings.

:param pdf_id: The unique identifier for the PDF.
:param pdf_path: The file path to the PDF.

Example Usage:

create_embeddings_for_pdf('123456', '/path/to/pdf')
"""
def create_embeddings_for_pdf(pdf_id: str, pdf_path: str):
    
    # Initialize a text splitter that breaks text into chunks of 500 characters with 100 character overlap,it is a set up of chunk.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
    )

    # Initialize PDF loader
    loader = PyPDFLoader(pdf_path)
    # Load and split PDF content with the text splitter into chunks
    docs = loader.load_and_split(text_splitter)
    # Add the chunks to the vector store

    for doc in docs:
        doc.metadata = {
            'page': doc.metadata['page'],
            'text': doc.page_content,
            'pdf_id': pdf_id,
        }
        
    vector_store.add_documents(docs)
    print("docs",docs)
