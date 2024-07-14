# Set your OpenAI API key
import os
import openai
os.environ["OPENAI_API_KEY"] = "sk-proj-***********************************"

# Importing Libraries
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext,load_index_from_storage

# define a class RAG
class RAG:
    def __init__(self, index):
        self.index = index

    def query(self,Questions):
        documents = SimpleDirectoryReader('data').load_data()
        index = VectorStoreIndex(documents,show_progress=True)
        # store data in local directory
        index.storage_context.persist(persist_dir="Embeddings")

        # load data from local directory
        storage_context = StorageContext.from_defaults(persist_dir="Embeddings")
        index = load_index_from_storage(storage_context)
        querry_engine = index.as_query_engine()

        response = querry_engine.query(Questions)   

        return response

# let's ask question
obj = RAG("data")
print(obj.query("List down names of all canidates?"))