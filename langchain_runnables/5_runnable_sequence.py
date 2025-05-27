# We need LLM to generate a joke on given topic and then explain the joke as well.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='explain the following joke \n {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

chain2 = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result2 = chain2.invoke({'topic':'cricket'})

print(result2)