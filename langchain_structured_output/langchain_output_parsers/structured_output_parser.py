from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI # If model does not open
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema # Not present in langchain_core but langchain itself.

from dotenv import load_dotenv

load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id='google/gemma-2-2b-it',
#     task='text-generation'
# )

# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 facts about {topic} \n {format_instructions}",
    input_variables=['topic'],
    partial_variables={'format_instructions': parser.get_format_instructions()}
)


# Without chaining - 

# prompt = template.invoke({'topic': 'black hole'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)


# With chaining - 

chain = template | model | parser

final_result = chain.invoke({'topic': 'black hole'})

print(final_result)