import streamlit as st
import requests


API_URL = "http://localhost:8000/api/chat"  


def send_message_to_server(message: str) -> str:
    """Send a user message to the FastAPI decision agent and return the response."""
    try:
        response = requests.post(API_URL, json={"message": message})
        if response.status_code == 200:
            return response.json().get("response", "No response returned.")
        else:
            return f"Error {response.status_code}: Could not get response."
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"


st.set_page_config(page_title="AI Customer Support Chat", page_icon="🤖")
st.title("🤖 AI Customer Support Chat")


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        with st.chat_message("user"):
            st.markdown(chat["content"])
    else:
        with st.chat_message("assistant"):
            st.markdown(chat["content"])

if user_input := st.chat_input("Type your message here..."):
    # Display user's message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    
    with st.chat_message("assistant"):
        response = send_message_to_server(user_input)
        st.markdown(response)
        # Save AI response to chat history
        st.session_state.chat_history.append({"role": "assistant", "content": response})