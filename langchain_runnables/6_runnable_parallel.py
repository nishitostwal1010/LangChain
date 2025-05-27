# We will use 2 LLMs in parallel, one to generate a tweet and second to generate a LinkedIn post on given topic.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a LinkedIn post about {topic}',
    input_variables=['topic']
)

model1 = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

model2 = ChatCohere(model='command-r')

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model1, parser),
    'post': RunnableSequence(prompt2, model2, parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print('-'*200)
print(result['post'])