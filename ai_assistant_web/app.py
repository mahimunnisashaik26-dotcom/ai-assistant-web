import streamlit as st
import requests

# 🔑 API KEY (from Streamlit Secrets)
API_KEY = st.secrets["API_KEY"]

# -------- PAGE CONFIG --------
st.set_page_config(page_title="AI Assistant Pro", layout="wide")

# -------- SESSION STATE --------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "history" not in st.session_state:
    st.session_state.history = []

# -------- SIDEBAR --------
with st.sidebar:
    st.title("📜 Chat History")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []

    if st.button("🆕 New Chat"):
        st.session_state.history.append(st.session_state.messages.copy())
        st.session_state.messages = []

    st.markdown("---")

    for i, chat in enumerate(st.session_state.history):
        if st.button(f"Chat {i+1}"):
            st.session_state.messages = chat

# -------- HEADER --------
st.title("🤖 AI Assistant Pro")
st.caption("ChatGPT-like AI Assistant")

# -------- DISPLAY CHAT --------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------- AI FUNCTION --------
def get_ai_response(text):
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openrouter/auto",  # best auto model
                "messages": [{"role": "user", "content": text}]
            }
        )

        result = response.json()

        # ✅ Safe response handling
        if "choices" in result:
            return result["choices"][0]["message"]["content"]
        else:
            return f"⚠️ API Error: {result}"

    except Exception as e:
        return f"⚠️ Error: {e}"

# -------- INPUT --------
user_input = st.chat_input("💬 Ask anything...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = get_ai_response(user_input)

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()
