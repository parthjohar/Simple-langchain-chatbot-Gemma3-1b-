# Simple LangChain Chatbot using Gemma 3:1b

This is a lightweight chatbot built using [LangChain](https://www.langchain.com/) and the `gemma:3b` model served via [Ollama](https://ollama.com). It uses a simple prompt-response pipeline and a Streamlit interface for interaction.

## Features

- Uses the `gemma:3b` open-source LLM via Ollama (no API cost)/`OpenAI` code also available in app.py(Paid).
- Streamlit-based UI for easy interaction.
- Modular LangChain setup using:
  - `ChatPromptTemplate`
  - `StrOutputParser`
  - `Ollama` LLM wrapper

## Setup Instructions

1. **Install dependencies:**
   ```bash
     pip install -r requirements.txt
2. **Install and run**
   ```bash
    ollama run gemma:3b
3.**Run the Chatbot**
  ```bash
    streamlit run Chatbot/app.py


