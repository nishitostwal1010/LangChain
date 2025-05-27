# We are generating a joke and then printing it(using passthrough) and using LLM to explain it parallely.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template='Give me a joke on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the joke given below \n {joke}',
    input_variables=['joke']
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

joke_generator_chain = RunnableSequence(prompt1, model, parser)

joke_and_explanation_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(joke_generator_chain, joke_and_explanation_chain)

result = final_chain.invoke({'topic':'cricket'})

print(result['joke'])
print('-'*200)
print(result['explanation'])