from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

### Basic-

# model = ChatOpenAI(model="gpt-4.1-nano")

# result = model.invoke("What is the capital of India")

# print(result)

# print(result.content)

### Low temperature-

# model = ChatOpenAI(model='gpt-4.1-nano', temperature=0)
# result = model.invoke("Suggest me 4 Indian male names")
# print(result.content)

### High temperature -

# model = ChatOpenAI(model='gpt-4.1-nano', temperature=1.8)
# result = model.invoke("Suggest me 4 Indian male names")
# print(result.content)

### Max_Completion_Tokens -

# Example 1:

# model = ChatOpenAI(model='gpt-4.1-nano', temperature=1.5, max_completion_tokens=10)
# result = model.invoke("Write a 5 line poem on cricket")
# print(result.content)

# Example 2:

model = ChatOpenAI(model='gpt-4.1-nano', temperature=1.5, max_completion_tokens=30)
result = model.invoke("Write a 5 line poem on cricket")
print(result.content)
