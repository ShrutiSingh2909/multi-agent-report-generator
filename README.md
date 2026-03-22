# 🤖 Multi-Agent AI Report Generator

![Python](https://img.shields.io/badge/Python-3.13-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-purple)
![Groq](https://img.shields.io/badge/Groq-LLaMA_3.3-orange)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_Memory-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

##  Overview

An end-to-end **Multi-Agent AI System** that autonomously researches, analyzes, and generates comprehensive downloadable PDF reports on any given topic.

The system uses **4 specialized AI agents** powered by **CrewAI** and **Groq LLaMA 3.3**, each with a specific role — researching the web, analyzing findings, writing a structured report, and reviewing the final output.

---

##  System Architecture
```
User (Streamlit UI)
        ↓
DuckDuckGo Search      ← Free web search, no API key needed
        ↓
Research Agent         ← Searches & collects raw information
(CrewAI + Groq LLM)
        ↓
Chroma Vector DB       ← Stores & retrieves research memory
        ↓
Analyst Agent          ← Finds key insights & patterns
        ↓
Writer Agent           ← Structures the full report
        ↓
FPDF Report Generator  ← Creates downloadable PDF
        ↓
User Downloads Report
```

---

##  Project Structure
```
multi-agent-report-generator/
├── agents/
│   ├── researcher.py       # Senior Research Analyst agent
│   ├── analyst.py          # Data Analyst agent
│   ├── writer.py           # Professional Report Writer agent
│   └── reviewer.py         # Quality Reviewer agent
├── tools/
│   ├── search_tool.py      # DuckDuckGo web search tool
│   └── memory_tool.py      # ChromaDB vector memory tool
├── core/
│   ├── crew.py             # CrewAI orchestration
│   └── pdf_generator.py    # FPDF report generation
├── app.py                  # Streamlit UI
├── .env                    # API keys (not committed)
├── .gitignore
└── requirements.txt
```

---

##  Agent Roles

### 1️ Research Agent
- Searches the web using DuckDuckGo
- Collects comprehensive facts and statistics
- Saves findings to ChromaDB vector memory

### 2️ Analyst Agent
- Retrieves research from ChromaDB
- Identifies key trends and patterns
- Extracts important statistics and insights

### 3️ Writer Agent
- Structures a professional report
- Covers: Executive Summary, Key Findings, Detailed Analysis, Trends, Challenges, Future Outlook, Conclusion

### 4️ Reviewer Agent
- Reviews report for accuracy and completeness
- Improves clarity and readability
- Returns final polished report

---

##  How to Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/multi-agent-report-generator.git
cd multi-agent-report-generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up API keys
Create a `.env` file:
```
GROQ_API_KEY=your-groq-api-key-here
```
Get your free Groq API key at: https://console.groq.com

### 4. Run the app
```bash
streamlit run app.py
```

### 5. Generate a report
- Enter any topic (e.g. `Impact of AI in Healthcare India`)
- Click **Generate Report**
- Wait 3-5 minutes for agents to complete
- Download your PDF report!

---

## Requirements
```
crewai
crewai-tools
chromadb
streamlit
fpdf2
langchain-google-genai
python-dotenv
ddgs
litellm
```

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core language |
| CrewAI | Multi-agent orchestration |
| Groq LLaMA 3.3 | LLM brain for all agents |
| ChromaDB | Vector database for agent memory |
| DuckDuckGo Search | Free web search tool |
| Streamlit | Interactive UI |
| FPDF2 | PDF report generation |
| LiteLLM | LLM provider abstraction |

---

##  Key Features

-  **Fully autonomous** — agents work without human intervention
-  **Real-time web search** — always up to date information
-  **Vector memory** — agents share knowledge via ChromaDB
-  **PDF download** — professional formatted report
-  **100% free** — no paid API needed
-  **Any topic** — works for any research topic

---

## 📊 Sample Output

**Input**: `Impact of Machine Learning in Healthcare`

**Output**: A structured PDF report covering:
- Market size ($36.1 billion by 2028)
- Key applications (medical imaging, diagnosis, personalized medicine)
- Challenges (data quality, regulatory frameworks, cybersecurity)
- Future outlook (deep learning, cloud platforms, explainability)

---

## 👩‍💻 Author

**Shruti**
- GitHub: [@ShrutiSingh2909](https://github.com/ShrutiSingh2909)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
