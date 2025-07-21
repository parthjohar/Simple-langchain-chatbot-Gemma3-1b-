import os 
from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.output_parsers import StrOutputParser

# Load env vars
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
langchain_api_key = os.getenv("LANGCHAIN_API_KEY")

print("OpenAI API Key:", openai_api_key)



# LangChain settings
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
os.environ["OPENAI_API_KEY"] = openai_api_key

# Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# Streamlit UI
st.title("LangChain Demo with OpenAI API")
input_text = st.text_input("Enter your question here")

# LLM setup
llm = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Invoke on input
if input_text:
    st.write("Response:")
    st.write(chain.invoke({"question": input_text}))
