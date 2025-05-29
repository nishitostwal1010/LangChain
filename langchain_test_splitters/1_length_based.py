from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Splitting smaple text -

# text = '''
# Artificial Intelligence (AI) is transforming industries worldwide. From healthcare and education to finance and manufacturing, AI-powered tools are enabling more efficient operations, predictive analytics, and enhanced customer experiences.
# One major breakthrough in AI is Natural Language Processing (NLP), which allows machines to understand and generate human language. Popular applications include chatbots, voice assistants like Alexa and Siri, and advanced search engines.
# Another key area is computer vision, which focuses on enabling machines to interpret visual information. Self-driving cars, facial recognition, and medical imaging are some notable applications.
# Despite its advancements, AI also raises ethical concerns. Issues such as bias in algorithms, job displacement, and data privacy must be addressed through proper regulations and transparency.
# In conclusion, while AI offers immense benefits, it requires thoughtful implementation and continuous monitoring to ensure it serves humanity responsibly.
# '''

# splitter = CharacterTextSplitter(
#     chunk_size = 100,
#     chunk_overlap = 0,
#     separator=''
# )

# result = splitter.split_text(text)

# for chunk in result:
#     print(chunk)
#     print('-'*160)


# Loading text from pdf and splitting it -

loader = PyPDFLoader('file.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[0])