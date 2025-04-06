from langchain.chains import ConversationalRetrievalChain
from app.chat.models import ChatArgs
from app.chat.vector_stores.pinecone import build_retriever
from app.chat.memories.sql_memory import build_memory
from app.chat.llms.chatopenai import build_lls

def build_chat(chat_args: ChatArgs):
   retriever = build_retriever(chat_args) 
   llm = build_lls(chat_args)
   memory = build_memory(chat_args)
   
   return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
    )
    
