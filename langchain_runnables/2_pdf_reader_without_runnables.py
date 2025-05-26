# This code is only for explanation not used now, we use different packages now.

from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import openai
from langchain.chains import RetrievalQA # Used to make retrieval task chain.

# Load the document
loader = TextLoader('docs.txt')
documents = loader.load()

# Split the text into smaller chunks
text_spiltter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
docs = text_spiltter.split_documents(documents)

# Convert text into embeddings & store in FAISS
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())

# Create a retriever (fetches relevant documents)
retriever = vectorstore.as_retriever()

# Initialize the LLM
llm = openai(model_name='gpt-3.5-turbo', temperature=0.7)

# Without chaining -

# # Manually Retrieve Relevant Documents
# query = "What are the key takeaways from the document?"
# retrieved_docs = retriever.get_relevant_documents(query)

# # Combine Retrieved Text into a Single Prompt
# retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])

# # Manually Pass Retrieved Text to LLM
# prompt = f"Based on the follwing text, answer the question: {query}\n\n{retrieved_text}"
# answer = llm.predict(prompt)

# # Print the answer
# print("Answer", answer)


# With chaining - 

# Using RetrievalQA chain we do not need to manually retrieve relevant documents combine them and pass query and retrieved text to llm everything is done by it.

# Create RetrievalQAChain
qa_chain = RetrievalQA.from_chain_type(llm=llm, retreiver=retriever)

# Ask a question
query = "What are the key takeways from the document?"
answer = qa_chain.run(query)

print('Answer: ', answer)