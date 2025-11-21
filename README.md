
# 🔍 Tavily-Powered Search Chatbot

*A minimal, modular chatbot built with Streamlit + LangChain*
**Author: Lakshya Pandit**

---

This project is a lightweight, cleanly organized chatbot that performs real-time web searches using **Tavily** and displays results inside a **Streamlit chat interface**.
The architecture follows good software design practices, making it easy to extend with LLMs, memory, tools, or additional chains.

---

## 📁 Project Layout

```
project/
│
├── core/
│   ├── interfaces.py          # Base interface for search components
│   ├── search_chain.py        # LangChain-compatible search executor
│   └── tavily_tool.py         # Utility for initializing Tavily client
│
├── app.py                     # Streamlit application (UI layer)
├── requirements.txt
├── .env
├── .python-version
└── README.md
```

---

## 🧠 Overview

### ✔ Clean Architecture

The logic is split into three layers:

| Layer                              | Responsibility                               |
| ---------------------------------- | -------------------------------------------- |
| **UI** (`app.py`)                  | Only handles Streamlit UI and chat flow      |
| **Core Logic** (`search_chain.py`) | Executes search queries using Tavily         |
| **Interfaces** (`interfaces.py`)   | Defines standard contract for search modules |

This separation makes the code easy to maintain and extend.

### ✔ Tavily Search

The chatbot sends queries to Tavily and returns structured results
(answer, citations, links, etc.).

### ✔ LangChain Ready

The search logic is implemented as a LangChain-style component, enabling:

* tool integration
* agents
* future LLM chains
* RAG-style workflows

---

## ⚙️ Setup Instructions

### 1️⃣ Python Version

Use pyenv to install the correct Python version:

```bash
pyenv install 3.11.6
pyenv local 3.11.6
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install Packages

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
TAVILY_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Your browser will open the chatbot interface automatically.

---

## 🧱 Architecture Notes

* **Single Responsibility:**
  Each file handles one task (UI, logic, interfaces).

* **Extensible:**
  You can plug in any other search engine or LLM by implementing the interface.

* **Replaceable Components:**
  Anything that follows `SearchInterface` can be swapped without changing the app.

---

## 🚀 Ideas for Future Work

* Add LLM responses summarizing Tavily results
* Incorporate memory or conversation context
* Add tool selection or agent-style reasoning
* Deploy to Streamlit Cloud or HuggingFace Spaces

---

## ✨ Author

**Created by: Lakshya Pandit**
Feel free to fork, experiment, and build on top of this foundation.


