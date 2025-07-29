import streamlit as st
from streamlit_smarttext_input import st_smart_text_input

st.set_page_config(page_title="SmartText Chat Thread", layout="centered")
st.title("Streamlit SmartText Chat")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Options (can be dynamic)
options = ["hi", "hello", "help", "bye", "thanks", "how are you?"]

# Display existing chat
st.markdown("### Conversation")
for i, msg in enumerate(st.session_state.chat_history):
    is_user = msg["sender"] == "user"
    with st.chat_message("user" if is_user else "assistant"):
        st.markdown(msg["text"])

# User input (free-form or from options)
user_input = st_smart_text_input(
    label="Type your message",
    options=options,
    placeholder="Ask something or say hello...",
    delay=100,
    disabled=False,
    label_visibility="collapsed",
    key=f"chat_input_{len(st.session_state.chat_history)}"

)

# When user submits a message
if user_input:
    # Add user message to history
    st.session_state.chat_history.append({
        "sender": "user",
        "text": user_input,
    })

    # Simple bot logic (replace with your own model later)
    if user_input.lower() in ["hi", "hello", "hey"]:
        bot_reply = " Hello, I am a Python package crafted by [Ankit Guria](https://github.com/ankit142)! How can I help you today?"
    elif "help" in user_input.lower():
        bot_reply = "Sure! I'm here to assist. Ask me anything."
    elif user_input.lower() in ["bye", "goodbye"]:
        bot_reply = " Goodbye! Have a great day."
    else:
        bot_reply = f"I heard you say: '{user_input}'"

    # Add bot reply to history
    st.session_state.chat_history.append({
        "sender": "bot",
        "text": bot_reply,
    })

    # Force rerun to refresh chat display and clear input
    st.rerun()
