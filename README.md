# 🏥 Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS

Ce projet est un **chatbot médical intelligent** basé sur **LangChain** et **Pinecone**, enrichi avec :
- 🌐 **Ngrok** pour exposer l’application localement
- 🤖 **Support multi-modèles LLM** avec sélection dynamique par l’utilisateur
- ☁️ **Déploiement CI/CD AWS** avec GitHub Actions

---

## 🚀 How to run?
### STEPS:

---

## 1 Clone the repository

```bash
git clone https://github.com/entbappy/Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS.git
cd Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS

## 2 Install dependencies
pip install -r requirements.txt

## 3 Create .env file

Create a .env file in the root directory and add:

PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

## 4 Store embeddings in Pinecone
python store_index.py


## 5 Run the Flask application
python app.py


Open in your browser:

http://localhost:5000

## 6 Multi-Model LLM Support

The application allows users to select the AI model dynamically from the UI.

Supported Models

Llama 3.3 – 70B

GPT OSS – 120B

Llama 4 Maverick – 17B

Qwen 3 – 32B (Medical Expert)

Llama 3.1 – 8B (Fast)

Kimi K2 – Long Context

Model Selector (UI)
<div class="model-selector">
  <label for="modelSelect">
    <i class="fas fa-robot"></i> AI Model:
  </label>
  <select id="modelSelect" class="custom-select">
    <option value="llama-3.3-70b-versatile">Llama 3.3 70B</option>
    <option value="openai/gpt-oss-120b">GPT OSS 120B</option>
    <option value="meta-llama/llama-4-maverick-17b-128e-instruct">
      Llama 4 Maverick 17B
    </option>
    <option value="qwen/qwen3-32b">Qwen 3 32B – Medical Expert</option>
    <option value="llama-3.1-8b-instant">Llama 3.1 8B Fast</option>
    <option value="moonshotai/kimi-k2-instruct-0905">
      Kimi K2 – Long Context
    </option>
  </select>
</div>

## 7 Architecture Overview
User
 ↓
Flask Web UI
 ↓
LangChain (RAG Pipeline)
 ↓
Pinecone Vector DB
 ↓
Selected LLM (Dynamic)

## 8 Tech Stack Used

Python

LangChain

Flask

Pinecone

Multiple LLMs (OpenAI, LLaMA, Qwen, etc.)

Ngrok

Docker

AWS (EC2, ECR)

GitHub Actions
