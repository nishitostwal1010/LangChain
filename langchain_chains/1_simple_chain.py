# from langchain_openai import ChatOpenAI
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# model = ChatOpenAI(model='gpt-4.1-nano')
model = GoogleGenerativeAI(model='gemini-2.0-flash')

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'M.S. Dhoni'})

print(result)

chain.get_graph().print_ascii()
