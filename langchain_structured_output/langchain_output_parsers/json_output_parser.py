from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint 
from langchain_google_genai import ChatGoogleGenerativeAI # if open model does not work 
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id='google/gemma-2-2b-it',
#     task='text-generation'
# )

# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash') # if open model does not work

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a fictional person. \n {format_instruction}",
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()} # Partial varaibles are the variable which are not decided at run-time but at compile-time. As the JsonOutputParser is parsing the instrcutions at compile-time itself.
)


# Without chaining - 

# prompt = template.format()
# # prompt = template.invoke({}) # If we need to use invoke then at least one input should be there if there are no input then pass an empty dictionary.

# result = model.invoke(prompt)

# final_result = parser.parse(result.content) # We are parsing the content inside the JSON objct we got.

# print(final_result)
# print(type(final_result))


# With chaining - 

chain = template | model | parser

result = chain.invoke({})

print(result)
