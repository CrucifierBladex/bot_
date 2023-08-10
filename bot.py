import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="Data-X Chatbot",
    page_icon="🤖",
    layout="wide",  # This allows for a wider layout
)

# Set a background color and center-align the content
st.markdown(
    """
    <style>
    body {
        background-color: #1f2937;
        color: white;
    }
    .stApp {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Add logo at the top
logo_image = "data-X-Prof.png"  # Provide the path to your logo image
st.image(logo_image, use_container_width=True)

# Set a title with custom styling
st.title("DataSciencePro Chatbot")
st.header("🤖 AI-powered Conversations")

# API endpoint and headers
endpoint = 'https://api.writesonic.com/v1/botsonic/botsonic/generate/d27869a1-c59e-4911-84ef-e12880070aae'
headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'python-requests/2.28.1',
    'accept': 'application/json',
    'token': '96e6a1e0-6370-47e7-81ec-d8effcea0b72',
}

# User input
st.write("Enter your questions below:")
question = st.text_input("You:", value="", key="input")

# Ask button with custom styling
if st.button("🚀 Ask"):
    if question:
        json_data = {
            'question': question,
            'chat_history': [],
        }

        response = requests.post(endpoint, headers=headers, json=json_data)

        try:
            response_data = response.json()
            answer = response_data[0]['data']['answer']
            st.text_area("Data-X:", answer, key="output", height=150)
        except (ValueError, KeyError):
            st.error("An error occurred while processing the response.")

#st.text("Type 'exit' to stop the chat.")
