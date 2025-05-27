# We are generating a joke using LLM then printing it(using passthrough) and counting words in it(using lambda) parallely.

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()   

prompt = PromptTemplate(
    template='Generate a joke on the {topic}',
    input_variables=['topic']
)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt, model, parser)

# Method 1: Using defined function

# def word_counter(text):
#     return len(text.split())

# parallel_chain = RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'word_count': RunnableLambda(word_counter) 
# })

# Method 2: Using lambda function

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(lambda x: len(x.split())) 
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({'topic':'AI'})

print(result['joke'])
print('-'*10)
print(result['word_count'])