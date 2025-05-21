from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="My ChatBot")
st.header("My ChatBot")

# Initialize chat history using Streamlit's session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant")
    ]

# Initialize messages display list
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear chat history button
def clear_chat_history():
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful AI assistant")
    ]
    st.session_state.messages = []

st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Input from user
user_input = st.chat_input("Enter your prompt:")

if user_input:
    # Add user message to history
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Initialize model and get response
    try:
        # Check if GOOGLE_API_KEY is set
        if not os.environ.get("GOOGLE_API_KEY"):
            st.error("GOOGLE_API_KEY environment variable not set.  Please set it in your .env file.")
            st.stop()

        model = ChatGoogleGenerativeAI(model='gemini-2.0-flash')
        response = model.invoke(st.session_state.chat_history)

        # Add AI response to history
        st.session_state.chat_history.append(AIMessage(content=response.content))
        st.session_state.messages.append({"role": "assistant", "content": response.content})

        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response.content)


    except Exception as e:
        st.error(f"An error occurred: {e}")
