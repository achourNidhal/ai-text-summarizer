# AI Text Summarizer API

A simple REST API that summarizes text into **5 bullet points** using Large Language Models (LLMs).

The API supports **two providers**:

- ☁️ OpenAI (cloud LLM)
- 💻 Ollama (local LLM)

This project demonstrates:

- LLM API integration
- Prompt engineering
- REST API development
- Local AI model integration

Built with **FastAPI** and Python.

---

# Tech Stack

- Python
- FastAPI
- OpenAI API
- Ollama
- Uvicorn

---

# Project Structure

ai-text-summarizer

├── main.py
├── requirements.txt
├── .env
└── README.md

---

# Installation

## 1. Clone the repository

git clone https://github.com/yourusername/ai-text-summarizer.git

cd ai-text-summarizer

---

## 2. Create a virtual environment

python -m venv venv

Activate the environment:

Windows (PowerShell)

.\venv\Scripts\Activate

Mac/Linux

source venv/bin/activate

---

## 3. Install dependencies

pip install -r requirements.txt

---

# Environment Variables

Create a `.env` file in the project root:

OPENAI_API_KEY=your_api_key_here

You can get your API key from the OpenAI platform.

---

# Running the API

Start the server with:

uvicorn main:app --reload

The API will run at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs

---

# API Endpoints

## 1️⃣ Summarize using OpenAI

POST /summarize/openai

Example request:

{
"text": "Artificial intelligence is transforming industries by automating tasks and improving decision making."
}

Example response:

{
"provider": "openai",
"summary": "- AI is transforming industries\n- Automation increases efficiency\n- Machine learning improves decisions\n- Data-driven strategies are growing\n- Ethical concerns are emerging"
}

---

## 2️⃣ Summarize using Ollama (Local LLM)

POST /summarize/ollama

Example request:

{
"text": "Artificial intelligence is transforming industries by automating tasks and improving decision making."
}

Example response:

{
"provider": "ollama",
"summary": "- AI transforms industries\n- Automation improves productivity\n- Companies adopt machine learning\n- Data drives innovation\n- Ethical considerations arise"
}

---

# Running Ollama Locally

Install Ollama from:

https://ollama.com

Download a model:

ollama pull llama3

Run the model:

ollama run llama3

Ollama exposes a local API used by this project:

http://localhost:11434

---

# Requirements

Example requirements.txt

fastapi
uvicorn
openai
requests
python-dotenv

---

# Example Use Cases

- AI-powered summarization service
- LLM backend API
- Learning project for integrating LLMs
- Demonstration of local
