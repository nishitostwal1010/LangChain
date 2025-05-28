from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='Social_Network_Ads.csv')

docs = loader.load()

print(len(docs)) # No of docs = No of rows
print('-'*200)
print(docs[0])
print('-'*200)
print(docs[0].page_content)