from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# Creating chat template
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful customer supprot agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}')
])

# Loading chat history from chat_history.txt
chat_history = []
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())
print(chat_history)

# Create prompt
prompt = chat_template.invoke({'chat_history': chat_history, 'query': 'Where is my refund'})

print(prompt)