# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from langchain_google_genai import ChatGoogleGenerativeAI # if open model does not work 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id='google/gemma-2-2b-it',
#     task='text-generation'
# )

# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash') # if open model does not work

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd promt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following {text}',
    input_variables=['text']
)


#Without StrOutputParser -

# prompt1 = template1.invoke({'topic': 'black_hole'})
# result1 = model.invoke(prompt1)

# prompt2 = template2.invoke({'text': result1.content})
# result2 = model.invoke(prompt2)

# print(result2.content)


# With StrOutputParser - 
# Here we created an object of StrOutputParser which is going to extract content from model output then we constrcuted a chain and then finally invoke the chain and gave the initial input everything else was done automatically.

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)
