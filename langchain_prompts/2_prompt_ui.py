# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt


# Static prompt -

# load_dotenv()

# model = ChatOpenAI(model='gpt-4.1-nano-2025-04-14')

# st.header("Research Tool")

# user_input = st.text_input("Enter your prompt")

# if st.button("Summarize"):
#     result = model.invoke(user_input)
#     st.write(result.content)


# Dynamic prompt (Method 1 - Defining the prompt here itself) -

# load_dotenv()

# model = ChatOpenAI(model='gpt-4.1-nano-2025-04-14')

# st.header('Research Tool') 

# paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

# style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

# length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# template = PromptTemplate(
#     template="""
#     Please summarize the research paper titled "{paper_input}" with the following specifications:
#     Explanation Style: {style_input}
#     Explanation Length: {length_input}
#     1. Mathematical Details:  
#         - Include relevant mathematical equations if present in the paper.
#         - Explain the mathematical concepts using simple, intuitive code snippets where applicable. 
#     2. Analogies: 
#         - Use relatable analogies to simplify complex ideas. 
#     If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
#     Ensure the summary is clear, accurate, and aligned with the provided style and length.
#     """,
#     input_variables=['paper_input', 'style_input', 'length_input']
# )

# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })

# if st.button('Summarize'):
#     result = model.invoke(prompt)
#     st.write(result.content)

# Dynamic prompt (Method 2 - Saving template in some other place) -

load_dotenv()

# model = ChatOpenAI(model='gpt-4.1-nano-2025-04-14')
model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')

st.header('Research Tool') 

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json') #Template is loaded from template.json

# Without chaining -

# prompt = template.invoke({
#     'paper_input': paper_input,
#     'style_input': style_input,
#     'length_input': length_input
# })

# if st.button('Summarize'):
#     result = model.invoke(prompt)
#     st.write(result.content)

# With chaining -

if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input': paper_input,
        'style_input': style_input,
        'length_input': length_input
    })
    st.write(result.content)