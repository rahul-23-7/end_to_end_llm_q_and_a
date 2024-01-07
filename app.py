from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv() # loads variables from .env file

# Function to load OPENAI Model and get response
def get_openai_response(question):
    llm=OpenAI(openai_api_key = os.getenv('OPENAI_API_KEY'),model_name="text-davinci-003",temperature=0.5)
    #Create a medical specific prompt
    medical_prompt = "As a medical assistant AI, " + question
    # Get the response from the model
    response = llm(medical_prompt)
    return response




# Initialize streamlit app
st.set_page_config(page_title="Q&A demo")
st.header("Langchain Application")

input=st.text_input("Input: ",key="input")
response=get_openai_response(input)

submit=st.button("Ask the question")

# If ask button is clicked
if submit:
    st.subheader("The response is")
    st.write(response)

