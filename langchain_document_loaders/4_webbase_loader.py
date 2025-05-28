from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = WebBaseLoader('https://www.flipkart.com/zebronics-zeb-sharp-pro-2048-hd-webcam-built-in-microphone-usb-connectivity/p/itmc0806f3606ff8?pid=ACCGS37KMFFKHYGC&lid=LSTACCGS37KMFFKHYGCUU7ZU9&marketplace=FLIPKART&q=webcam&store=6bo%2Fai3%2Fr3e&spotlightTagId=default_TrendingId_6bo%2Fai3%2Fr3e&srno=s_1_8&otracker=search&otracker1=search&fm=Search&iid=78dadb42-e372-4ac6-993f-d08d8e0001f4.ACCGS37KMFFKHYGC.SEARCH&ppt=sp&ppn=sp&ssid=vxs86br59gln162o1747930764684&qH=86722fdb4bc3199d')

docs = loader.load()

# print(docs[0].page_content)
# print('-'*200)
# print(len(docs))

prompt = PromptTemplate(
    template='Answer the following question - \n {question} \n from the following text - \n {text}',
    input_variables=['question','text']
)

# model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash-preview-05-20')

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'question': 'Should I buy this webcam', 'text': docs[0].page_content})

print(result)