import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

def review_code(code):
    """Uses the Gemini API to analyze the given Python code."""
    prompt = f"""
    Review the following Python code and identify any potential bugs, errors, or areas of improvement. 
    Also, provide the corrected version of the code.
    
    Code:
    ```python
    {code}
    ```
    """
    
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    return response.text


st.title("GenAI - AI Code Reviewer")
st.write("Submit your Python code and get AI-generated bug reports and fixes.")
code_input = st.text_area("Enter your Python code here:", height=250)

if st.button("Review Code"):
    if code_input.strip():
        with st.spinner("Reviewing code..."):
            feedback = review_code(code_input)
        
        st.subheader("AI Feedback & Suggestions")
        st.write(feedback)
    else:
        st.warning("Please enter some Python code before submitting.")
