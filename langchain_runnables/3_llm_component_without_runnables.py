import random

### Sample LLM class -

# class NakliLLM:

#     def __init__(self):
#         print('LLM created')

#     def predict(self, prompt):

#         # We are not using api so we will return any of these sample responses for now
#         response_list = [
#             'Delhi is the capital of India',
#             'IPL is a cricket league',
#             'AI stands for Artificial Intelligence'
#         ]

#         return {'response': random.choice(response_list)}
    
# llm = NakliLLM()

# result = llm.predict('What is the capital of India')

# print(result)
# print(result['response']) # It is a normal dictionary so we can't use result.response as that is not applicable for simple dictionaries

##########

### Sample PromptTemplate class - 

# class NakliPromptTemplate:

#     def __init__(self, template, input_variables):
#         self.template = template
#         self.input_variables = input_variables

#     def format(self, input_dict):
#         return self.template.format(**input_dict)
    
# template = NakliPromptTemplate(
#     template='Write a {length} poem about {topic}',
#     input_variables=['length','topic']
# )

# prompt = template.format({'length':'short','topic':'India'})

# print(prompt)

##########

### Using these components together to make a LLM application - 

# class NakliLLM:

#     def __init__(self):
#         print('LLM created')

#     def predict(self, prompt):

#         # We are not using api so we will return any of these sample responses for now
#         response_list = [
#             'Delhi is the capital of India',
#             'IPL is a cricket league',
#             'AI stands for Artificial Intelligence'
#         ]

#         return {'response': random.choice(response_list)}

# class NakliPromptTemplate:

#     def __init__(self, template, input_variables):
#         self.template = template
#         self.input_variables = input_variables

#     def format(self, input_dict):
#         return self.template.format(**input_dict)

# llm = NakliLLM()

# template = NakliPromptTemplate(
#     template='Write a {length} poem about {topic}',
#     input_variables=['length', 'topic']
# )

# prompt = template.format({'length':'short', 'topic':'India'})

# print(prompt)

# result = llm.predict(prompt)

# print(result)
# print(result['response'])

##########

### Using multiple components each and every time is not easy that is the reason LangChain came with the concept of chains

##########

### Sample chain using the components -

class NakliLLM:

    def __init__(self):
        pass

    def predict(self, prompt):

        # We are not using api so we will return any of these sample responses for now
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]

        return {'response': random.choice(response_list)}

class NakliPromptTemplate:

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)

class NakliLLMChain:

    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt
    
    def run(self, input_dict):

        final_prompt = self.prompt.format(input_dict)

        result = self.llm.predict(final_prompt)

        return result['response']
    
llm = NakliLLM()

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

chain = NakliLLMChain(llm, template)

result = chain.run({'length':'short', 'topic':'India'})

print(result)

##########

### But making these chain classes is not beneficial as they are not flexible and we need to create a custom chain for each type of task-
# eg) LLMChain - prompt and LLM
# eg) RetrievalQA chain - for retrieval task

### As all the component classes were not standardized we need different methods for each component -
# .format() for PromptTemplate
# .predict() for LLM

### This was the reason LangChain thought of making standardized components and runnables were introduced.

