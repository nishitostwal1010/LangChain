from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding_model = OpenAIEmbeddings(model='text-embedding-3-small', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "Paris is the capital of France",
    "Berlin is the capital of Germany"
]

results = embedding_model.embed_documents(documents)

print(results, "\n")

for result in results:
    print(result, "\n")