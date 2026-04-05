import streamlit as st
from brain import process_command

st.set_page_config(page_title="AI Assistant", layout="centered")

st.title("🤖 AI Assistant")
st.caption("Smart Command Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input box
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = process_command(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()