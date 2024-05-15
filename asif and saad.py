# Necessary imports
import openai
from dotenv import load_dotenv
import streamlit as st
import os
import textwrap

# Load environment variables
load_dotenv()  

# Configure OpenAI API
openai.api_key = os.getenv("sk-proj-cq8oEgTJi99JUTUTVS05T3BlbkFJCzMVy8FKVvStMVVnAT8U")

# Function to get response from OpenAI's GPT-3 model
def get_gpt_response(question):
    response = openai.Completion.create(
      engine="davinci",  # You can choose another engine if you prefer
      prompt=question,
      max_tokens=150  # You can adjust this as needed
    )
    return response.choices[0].text.strip()

# Initialize Streamlit app
st.set_page_config(page_title="Saad & Asif ChatBot")
st.header("Chatbot by best friends")

# Input field for user question
input_text = st.text_input("Input: ", key="input")

# Button to submit the question
submit_button = st.button("Ask the question")

# If the submit button is clicked
if submit_button:
    # Get response from GPT-3 model
    response = get_gpt_response(input_text)
    # Display the response
    st.subheader("The Response is")
    st.write(response)
