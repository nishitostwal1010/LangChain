from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

class Person(BaseModel):

    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fictional {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions}
)


# Without chaining -

# prompt = template.invoke({'place': 'Indian'})
# print(prompt)
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

# Print prompt to see what form of prompt is passed to the model


# With chaining - 

chain = template | model | parser

result = chain.invoke({'place':'Indain'})

print(result)