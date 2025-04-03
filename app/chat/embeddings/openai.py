from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv


load_dotenv()

embeddings = OpenAIEmbeddings()