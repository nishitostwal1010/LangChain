from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

# Loading 'cricket.txt' text file using TextLoader -

# loader = TextLoader('cricket.txt', encoding='utf-8')

# docs = loader.load()

# print(docs)
# print(type(docs))
# print(len(docs))
# print(docs[0])
# print(type(docs[0])) 


# Using llm with loader

loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)