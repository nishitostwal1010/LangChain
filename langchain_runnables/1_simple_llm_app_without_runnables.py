# This code is only for explanation not used, we use different packages now. 

from langchain.llms import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain #Used to create Basic LLMChain(llm, prompt)

llm = openai(model='gpt-3.5-turbo-instruct', temperature=0.7)

prompt = PromptTemplate(
    template='Suggest a catchy blog title about {topic}.',
    input_variables=['topic']
)


# Without chaining -

# topic = input('Enter a topic: ')

# # formatted_prompt = prompt.invoke({'topic'}: topic)
# formatted_prompt = prompt.format(topic=topic)

# #blog_title = llm.invoke(formatted_prompt)
# blog_title = llm.predict(formatted_prompt)

# print('Generated Blog Title: '+blog_title)


# Using LLMChain(Most simple chain - contains prompt and llm) -

chain = LLMChain(llm=llm, prompt=prompt)

topic = input('Enter a topic')
output = chain.run(topic)

print('Generated Blog Title:', output)
