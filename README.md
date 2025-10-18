
# Local ReAct AI Agent with LangGraph & Ollama

A local-first AI agent framework using LangGraph and Ollama. Implements a ReAct-style reasoning loop with tool calling, external API integration, and step-by-step problem solving using local LLMs like LLaMA 3.1. Ideal for building private, extensible AI assistants.

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```
git clone https://github.com/EArdiles/react-agent-local-llm.git
cd react-agent-local-llm
```

### 2. Create and Activate a Virtual Environment

```
python -m venv .venv
# On macOS/Linux
source .venv/bin/activate
# On Windows
.venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run the LLM Model with Ollama

Make sure you have Ollama installed and running. Then, start the LLaMA 3.1 model:

```
ollama run llama3.1
```

> ⚠️ Replace `llama3.1` with the exact model tag if needed.

### 5. Run the Agent

```
python main.py
```

---

## 🧠 Features

- ReAct-style reasoning loop  
- Tool calling and external API integration  
- Local-first architecture for privacy and control  
- Built with LangGraph and powered by Ollama

---

## 📦 Requirements

- Python 3.9+  
- Ollama  
- LLaMA 3.1 model installed via Ollama
