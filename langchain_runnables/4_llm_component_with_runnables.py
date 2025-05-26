import random
from abc import ABC, abstractmethod #abc - Abstract Base Classes, ABC - Abstract Base Class, @abstractmethod - It is a decorator that marks a method as abstract.

class Runnable(ABC):

    @abstractmethod
    def invoke(input_data):
        pass

class NakliLLM(Runnable):

    def __init__(self):
        pass

    # As NakliiLLM is now an abtract class as it inherits Runnalbe so we need to define all the abstract methods in it.
    # The reason we are making a new method and not removing the previous method predict is that there might be some developers still using it.
    # We can print "This method is going to be depricated in future, use invoke instead." if someone uses previous method(i.e. predict in this case)"
    def invoke(self, promt): 
        # We are not using api so we will return any of these sample responses for now
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]

        return {'response': random.choice(response_list)}

    def predict(self, prompt):

        # We are not using api so we will return any of these sample responses for now
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]

        return {'response': random.choice(response_list)}

class NakliPromptTemplate(Runnable):

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict):
        return self.template.format(**input_dict)

    def format(self, input_dict):
        return self.template.format(**input_dict)
    
class NakliStrOutputParser(Runnable):

    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data['response']

class RunnableConnector(Runnable):

    def __init__(self, runnable_list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):

        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        
        return input_data
    
##########

# We make a RunnableConnector class in which we can pass multiple components and it will have a invoke method which will invoke each component passed using for loop and initial input_data is given to it. Then the output came from the first component is stored as input_data and now this input_data is passed for second component invoke and so on. Therefore at last the last component will invoke and the final output will be returned.

##########

### Executing chain using Runnable -

# template = NakliPromptTemplate(
#     template='Write a {length} poem about {topic}',
#     input_variables=['length','topic']
# )

# llm = NakliLLM()

# parser = NakliStrOutputParser()

# chain = RunnableConnector([template, llm, parser])

# result = chain.invoke({'length':'long', 'topic':'cricket'})

# print(result)

##########

### Executing multiple chains using Runnable -

template1 = NakliPromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

template2 = NakliPromptTemplate(
    template='Explain the following joke {response}',
    input_variables=['response']
)

llm = NakliLLM()

parser = NakliStrOutputParser()

chain1 = RunnableConnector([template1, llm])

chain2 = RunnableConnector([template2, llm, parser])

final_chain = RunnableConnector([chain1, chain2])

result = final_chain.invoke({'topic':'cricket'})

print(result)

# The reason I didn't pass parser in chain 1 is because chain 2 will take the output of chain 1 and that should be dictionary(PromptTemplate take dictionary as input but if you are using actual Runnable and component then you can use parser in between as I have done in previous codes as well)