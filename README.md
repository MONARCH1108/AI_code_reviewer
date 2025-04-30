# 🧠 AI Code Reviewer

A web-based AI-powered tool that reviews Python code, detects bugs, suggests improvements, and generates human-friendly documentation using language models.

---

## 📌 Overview

This project demonstrates the evolution of a code reviewer app through two versions:

- **Version 1**: Built with guidance from ChatGPT and tutorials. It uses Google's Gemini API and Streamlit for quick prototyping.
- **Version 2**: Fully self-written using Flask and a local Ollama LLM (`llama3.2`) for offline, more customizable AI processing.

---

## 🧾 Table of Contents

- [Project Structure](#file-structure)
- [Version Highlights](#version-highlights)
- [Tech Stack](#tech-stack)
- [Setup & Installation](#setup--installation)
- [How to Run](#how-to-run)
- [Learnings & Evolution](#learnings--evolution)
- [Screenshots](#screenshots) *(optional)*
- [License](#license)

---

## 📁 File Structure

```bash
.
├── version_1/                   # Streamlit + Gemini API version
│   ├── app.py
│   └── .env (Google API key)
│
├── version_2/                   # Flask + Ollama + Llama3.2 version
│   ├── app.py
│   ├── templates/
│   │   └── index.html
│   └── utils/
│       └── functions.py
│
├── README.md
└── requirements.txt             # Optional, depending on environment
```

## ✨ Version Highlights

### 🔹 Version 1 (Assisted Build)

- Built using **Streamlit** for fast UI.
    
- Uses **Google Gemini API** via `google.generativeai`.
    
- Offers simple input/output layout for quick feedback.
    

### 🔸 Version 2 (Self-Built)

- Built using **Flask** from scratch.
    
- Implements **Ollama** with a **locally running `llama3.2` model**.
    
- Enhanced prompt engineering for better review quality.
    
- Beautiful **custom HTML/CSS UI** for better user experience.
    
- Contains robust instructions for context filtering (code-only reviews).

|Area|Tools Used|
|---|---|
|Frontend|Streamlit (v1), HTML/CSS (v2)|
|Backend|Python, Flask|
|LLM|Google Gemini API (v1), Ollama LLM (`llama3.2`) (v2)|
|Environment|dotenv (`.env`), virtualenv|

## ⚙️ Setup & Installation

### 🧪 Version 1
```bash
cd version_1
python -m venv venv
source venv/bin/activate       # Windows: venv\Scripts\activate
pip install streamlit google.generativeai 
```

# Set your Google API Key in .env
```bash
echo GOOGLE_API_KEY=your_key_here > .env

streamlit run app.py
```

### 🛠️ Version 2
```bash
cd version_2
python -m venv venv
source venv/bin/activate
pip install flask ollama

# Make sure Ollama is installed and running
ollama run llama3.2

python app.py
```

## 🧠 Learnings & Evolution
### Version 1 
 - taught me the basics of API calls, prompt structuring, and how to quickly prototype with Streamlit.

### Version 2 
 - was my full-stack build using Flask, local LLMs, and custom UI — improving my understanding of backend routing, HTML templating, and deploying AI models locally.

<<<<<<< HEAD
- Implemented stricter prompt rules and better error handling in v2.
=======
Implemented stricter prompt rules and better error handling in v2.
>>>>>>> 1ae733177792846a0d0b7beb86e774f942fd634c
