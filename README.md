# 🤖 AI Customer Support Agent

An intelligent **AI-powered customer support system** that combines **Retrieval-Augmented Generation (RAG)**, **LLM reasoning**, and **tool-based decision making** to answer user queries efficiently.

The system retrieves answers from a **vector database of FAQs**, routes specific queries to **custom tools (order tracking and product info)**, and uses a **Large Language Model (LLM)** for general questions.

---

# 🚀 Features

* **RAG-based FAQ retrieval** using Chroma vector database
* **LLM fallback responses** for queries not found in the FAQ dataset
* **Tool-based query routing**

  * Order Tracking Tool
  * Product Information Tool
* **Conversation memory** using LangChain
* **FastAPI backend** for serving the AI agent
* **Streamlit chat interface** for user interaction
* **OpenAI embeddings** for semantic search

---

# 🏗 System Architecture

User → Streamlit Chat UI → FastAPI API → Decision Agent

Decision Agent routes the query to:

* Tool Router (Order Tracking / Product Info)
* Retrieval Engine (RAG using Chroma)
* LLM (GPT model)

Data Flow:

1. User sends a message through the Streamlit UI.
2. The request is sent to the FastAPI backend.
3. The Decision Agent determines the best response method:

   * Tool response
   * FAQ retrieval
   * LLM-generated answer
4. The response is returned and displayed in the chat interface.

---

# 📁 Project Structure

customer_support_agent

app
├── agent
│   ├── decision_agent.py
│   └── memory_manager.py

├── api
│   ├── chat_api.py
│   └── faq_api.py

├── rag
│   ├── chroma_db.py
│   ├── embedding_model.py
│   ├── faq_loader.py
│   ├── ingest_faq.py
│   └── retrieval_engine.py

├── tools
│   ├── order_tracking_tool.py
│   └── product_info_tool.py

data
└── faq_dataset.json

frontend
└── chat_app.py

main.py

---

# 🧠 Technologies Used

* **Python**
* **FastAPI**
* **Streamlit**
* **LangChain**
* **OpenAI API**
* **Chroma Vector Database**
* **Pydantic**

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/customer_support_agent.git
cd customer_support_agent
```

---

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

Required packages include:

* fastapi
* uvicorn
* streamlit
* langchain
* langchain-openai
* chromadb
* requests

---

### 4️⃣ Set OpenAI API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

---

# 🗂 Load FAQ Data into Vector Database

Run the ingestion script:

```bash
python -m app.rag.ingest_faq
```

This will:

* Convert FAQs into embeddings
* Store them in Chroma vector database

---

# ▶️ Running the Application

### Start FastAPI backend

```bash
uvicorn app.main:app --reload
```

API will run at:

```
http://localhost:8000
```

---

### Start Streamlit chat UI

```bash
streamlit run chat_app.py
```

---

# 💬 Example Queries

FAQ queries:

```
What is the return policy?
How long does shipping take?
```

Tool queries:

```
Track order 12345
Get product info 101
```

General queries:

```
What is a large language model?
Explain AI in simple terms
```

---

# 📊 Evaluation

The system was evaluated on:

* **Retrieval accuracy** for FAQ queries
* **Tool routing correctness**
* **LLM response quality**
* **API response latency**

Results show the system effectively combines **semantic retrieval and generative AI** to answer a wide range of customer support queries.

---

# 🔮 Future Improvements

* Intent classification for smarter tool routing
* Hybrid search (keyword + vector retrieval)
* Persistent conversation memory
* Authentication for API endpoints
* Analytics dashboard for monitoring queries

---

# 👩‍💻 Author

Faiza
AI Customer Support Agent Project
