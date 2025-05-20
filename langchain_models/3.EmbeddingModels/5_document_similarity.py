from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = input("Enter your query: ")


# My method: 

# docs_embeddings = embedding_model.embed_documents(documents)
# query_embedding = embedding_model.embed_query(query)

# query_vector = np.array(query_embedding).reshape(1, -1) # Cosine similarity expects 2D vector as input
# similarity_list = []

# for doc_embedding in docs_embeddings:
#     doc_vector = np.array(doc_embedding).reshape(1, -1)
#     similarity = cosine_similarity(doc_vector, query_vector)[0][0] # Cosine similarity returns 2D [[]]
#     similarity_list.append(similarity)

# index = similarity_list.index(max(similarity_list))

# print(f"The document which is most similar to the given query is:\n {documents[index]}")


# Actual method:

docs_embeddings = embedding_model.embed_documents(documents) 
query_embedding = embedding_model.embed_query(query)

similarity_scores = cosine_similarity(docs_embeddings, [query_embedding])

# We used enumerate to get index and values and stored them in list so that we can keep track of actual indexes.
# Then we used sorted function and specified key so that list is sorted according to values.
# Then we stored the last element in index and score variables. 
index, score = sorted(list(enumerate(similarity_scores)), key=lambda x:x[1])[-1]

print(documents[index])
print(f"The similarity between document and query is: {score}")

#We should store the document embedding so that we don't need to generate them again and again.