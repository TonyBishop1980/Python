import pip

import langchain



from langchain.llms import OpenAI
from langchain import document_loaders
from langchain.indexes import VectorIndex
import os

# Use a string for the file path
document_loaders = TextLoader("C:\\Users\\Tony Bishop\\Desktop\\Training\\data.txt")

# Retrieve the API key from an environment variable
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# Initialize the OpenAI object with the API key
llm = OpenAI(api_key=api_key)

vector_index = VectorIndex()
vector_index.index_data_loader(data_loader)

def query_custom_data(query):
    return vector_index.query(query, llm)

response = query_custom_data("Describe the companies of my internships")
print(response)


