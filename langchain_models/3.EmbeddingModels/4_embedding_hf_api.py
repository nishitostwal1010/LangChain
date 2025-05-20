from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

embedding = HuggingFaceEndpointEmbeddings(
    repo_id='sentence-transformers/all-MiniLM-L6-v2',
    huggingfacehub_api_token=os.getenv('HUGGINGFACEHUB_API_TOKEN') # Kuch to backchodi ho rahi hai isliye token directly de diya
)

# query = "Delhi is the capital of India"

# result = embedding.embed_query(query)

# print(result)

documents = [
    "Delhi is the capital of India",
    "Paris is the capital of France",
    "Berlin is the capital of Germany"
]

results = embedding.embed_documents(documents)

print(results, "\n")

for i, result in enumerate(results):
    print(f"Total length: {len(result)}")
    print(f"First 10 values(dim) of DOC {i+1}: {result[:10]}\n")
