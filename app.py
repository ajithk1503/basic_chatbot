from langchain_openai import ChatOpenAI
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="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"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful assistant.please respond to user queries"),
        ("user","Question:{question}")
    ]
)


st.title("Demo")
input_text=st.text_input("Search")

llm = OllamaLLM(model="llama3.2:1b")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
