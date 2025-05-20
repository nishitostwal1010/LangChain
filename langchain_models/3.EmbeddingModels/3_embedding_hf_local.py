from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# text = "Delhi is the capital of India"

# result = embedding.embed_query(text)

# print(result)

documents = [
    "Delhi is the capital of India",
    "Paris is the capital of France",
    "Berlin is the capital of Germany"
]

results = embedding.embed_documents(documents)

print(results, "\n")

for result in results:
    print(result, "\n")