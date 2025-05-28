from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# Using load -

# docs = loader.load()

# This for loop is going to take too much time as there are 600+ pages in ISLP and it will load all of them at once.
# for document in docs:
#     print(document.metadata)


# Using lazy_load -

docs = loader.lazy_load()

# This for loop will print pages as they are loaded.
for document in docs:
    print(document.metadata)