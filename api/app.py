from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]="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"

app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)
llm = OllamaLLM(model="llama3.2:1b")

# Define prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5‑year‑old child with 100 words")

# Add routes
add_routes(app, prompt1 | llm, path="/essay")
add_routes(app, prompt2 | llm, path="/poem")

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)