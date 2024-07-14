
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext, load_index_from_storage

from flask import Flask, request, render_template
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "sk-proj-****************************************"

app = Flask(__name__)

class RAG:
    def __init__(self):
        self.index = None

    def load_documents(self, data_dir):
        # Load documents from the specified directory using SimpleDirectoryReader
        documents = SimpleDirectoryReader(data_dir).load_data()
        print(f"Number of documents loaded: {len(documents)}")
        return documents

    def create_index(self, documents, persist_dir="Embeddings"):
        # Create a VectorStoreIndex from the documents
        index = VectorStoreIndex(documents, show_progress=True)
        # Persist the index to the specified directory
        index.storage_context.persist(persist_dir=persist_dir)
        return index

    def load_index(self, persist_dir="Embeddings"):
        # Load the index from the specified directory
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
        return index

    def query(self, question):
        # Load all documents from the 'data' directory
        documents = self.load_documents('data')
        if not self.index:
            self.index = self.create_index(documents)
        else:
            self.index = self.load_index()

        query_engine = self.index.as_query_engine()
        response = query_engine.query(question)
        return response

@app.route('/', methods=['GET', 'POST'])
def index():
    response = ""
    if request.method == 'POST':
        question = request.form['question']
        obj = RAG()
        response = obj.query(question)
    
    return render_template('index.html', response=response)

if __name__ == '__main__':
    app.run(debug=True)
