import streamlit as st
import openai

openai_api_key = st.secrets["openai"]["OPENAI_API_KEY"]

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
openai.api_key = openai_api_key

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    st.write(f"{message['role']}: {message['content']}")

# Accept user input
prompt = st.text_input("What is up?")

if st.button("Send"):
    if prompt:
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        st.write(f"user: {prompt}")

        # Get assistant response
        response = openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=st.session_state.messages,
        )

        assistant_message = response['choices'][0]['message']['content']
        
        # Display assistant response
        st.write(f"assistant: {assistant_message}")

        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
