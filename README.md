# GenAI - AI Code Reviewer

## Overview

GenAI - AI Code Reviewer is a Python-based web application that allows users to submit their Python code for review. The application utilizes Google's Gemini API to analyze the submitted code, identify potential bugs, errors, and areas of improvement, and provide corrected code snippets as suggestions.

## Features

- **Code Review**: Submit Python code to get AI-generated feedback.
    
- **Bug Detection**: Identify syntax errors, logical errors, and other potential issues.
    
- **Fix Suggestions**: Receive corrected versions of the code.
    
- **User-Friendly Interface**: Built using Streamlit for an intuitive and interactive experience.
    

## Tech Stack

- **Python**
    
- **Streamlit** (Frontend for UI)
    
- **Google Gemini API** (AI-powered code analysis)
    
- **Dotenv** (For API key management)
    

## Installation

### Prerequisites

Ensure you have Python installed on your system.

### Steps to Install

1. Clone the repository:
    
    ```
    git clone https://github.com/your-username/genai-code-reviewer.git
    cd genai-code-reviewer
    ```
    
2. Create and activate a virtual environment:
    
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
    
3. Install the required dependencies:
    
    ```
    pip install -r requirements.txt
    ```
    
4. Set up your API key:
    
    - Create a `.env` file in the root directory.
        
    - Add the following line to the `.env` file:
        
        ```
        GOOGLE_API_KEY=your_google_api_key_here
        ```
        

## Usage

Run the Streamlit app:

```
streamlit run app.py
```

