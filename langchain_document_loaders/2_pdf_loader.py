from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('file.pdf')

docs = loader.load()

print(len(docs)) # Same as number of pages in pdf as PyPDFloader makes a document object for each page of given pdf.

for doc in docs:
    print(doc)
    print('-'*200)
