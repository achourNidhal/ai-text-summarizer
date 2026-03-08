from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="AI Text Summarizer API")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class TextRequest(BaseModel):
    text: str


# -------------------------
# Endpoint 1 : OpenAI
# -------------------------
@app.post("/summarize/openai")
def summarize_openai(request: TextRequest):

    prompt = f"Summarize this text in 3 bullet points:\n{request.text}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return {
            "provider": "openai",
            "summary": response.choices[0].message.content
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------
# Endpoint 2 : Ollama
# -------------------------
@app.post("/summarize/ollama")
def summarize_ollama(request: TextRequest):

    prompt = f"Summarize this text in 3 bullet points:\n{request.text}"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Ollama error")

    result = response.json()

    return {
        "provider": "ollama",
        "summary": result["response"]
    }