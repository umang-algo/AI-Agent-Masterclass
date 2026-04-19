# AI Agent SDKs & Frameworks: The Master Course (2026 Edition) 🎓🚀

> **The definitive hands-on guide to building Autonomous Business Agents** — from concept to production, across 5 enterprise SDK ecosystems.

This course moves you beyond chatbots and into **Agentic Orchestration**. We don't just teach code; we solve real-world industry problems in **Marketing, Finance, Legal, HR, and Real Estate** using the most battle-tested agent frameworks available today.

---

## 🎯 Who This Course Is For

- **Senior Data Scientists & ML Engineers** ready to deploy multi-agent systems in production
- **Enterprise AI Practitioners** evaluating frameworks for their organization's stack
- **Developers** who have built simple LLM apps and want to advance to orchestrated agent pipelines
- **AI Architects** designing autonomous workflows across business functions

**Prerequisites:** Python proficiency, basic LLM API familiarity, and comfort with Jupyter notebooks.

---

## 🏗️ Course Architecture

The course is divided into **5 Chapters + 1 Capstone Project**, each focusing on a specific SDK ecosystem and a real-world **Business Case Study**.

### [Chapter 1: The Microsoft Ecosystem](./Chapter_1_Microsoft_Ecosystem.md)
- **Tools**: AutoGen `0.2.14`, Semantic Kernel `0.9.1`
- **Business Case 1**: 5-Agent Financial Boardroom — automated MSFT/TSLA Q3 earnings analysis with CFO, Analyst, Risk, Compliance, and Narrator agents debating in round-robin
- **Business Case 2**: Brand Compliance Plugin Pipeline — Semantic Kernel plugin chain enforcing tone, legal disclaimers, and formatting rules on marketing copy
- **Key Concepts**: Multi-agent chat, GroupChat termination conditions, SK plugin architecture, memory contexts

### [Chapter 2: The LangChain Ecosystem](./Chapter_2_LangChain_Ecosystem.md)
- **Tools**: LangChain `0.1.13`, LangGraph `0.0.26`, ChromaDB `0.4.24`, LangSmith `0.1.31`
- **Business Case 1**: 7-Section HR Knowledge Agent — RAG-powered HR handbook with vector retrieval, source attribution, and policy-aware Q&A
- **Business Case 2**: 7-Node Intelligent Support Router — LangGraph state machine routing tickets to Technical, Billing, or VIP Escalation paths with conditional branching
- **Key Concepts**: RAG pipelines, vector stores, LangGraph state graphs, conditional edges, observability tracing

### [Chapter 3: Native Provider Tooling](./Chapter_3_OpenAI_and_Google.md)
- **Tools**: OpenAI Assistants API `openai 1.14.2`, Google Gen AI SDK / ADK `google-cloud-aiplatform 1.44.0`
- **Business Case 1**: 3-Clause Legal Contract Auditor — OpenAI Assistant with file search analyzing indemnification, IP assignment, and non-compete clauses
- **Business Case 2**: 3-Market PropTech Investment Analysis — Google ADK agent analyzing SF, NYC, and Miami real estate markets with structured scoring
- **Key Concepts**: Assistant threads & runs, file attachments, function calling, Google ADK tool registration, structured JSON output

### [Chapter 4: Specialized Open-Source Frameworks](./Chapter_4_Specialized_Open_Source_Frameworks.md)
- **Tools**: CrewAI `0.22.4`, HuggingFace smolagents `0.0.1`
- **Business Case 1**: 4-Agent Marketing Swarm — CrewAI crew with Strategist, Copywriter, Designer, and Compliance agents collaborating on a campaign with hierarchical process
- **Business Case 2**: Multi-Region Tax Discrepancy Auditor — smolagents ReAct loop cross-referencing 5 transactions across US, EU, and APAC tax rules
- **Key Concepts**: CrewAI roles/goals/backstories, task delegation, smolagents tool creation, ReAct reasoning traces

### [Chapter 5: Enterprise & Low-Code Platforms](./Chapter_5_Enterprise_and_Low_Code_Platforms.md)
- **Tools**: Dify (hosted), n8n (self-hosted)
- **Business Case 1**: Headless Sales Concierge — Dify workflow exposed as REST API endpoint handling product qualification and CRM enrichment
- **Business Case 2**: VIP Incident Escalation Swarm — n8n webhook-triggered workflow with conditional branching, Slack notifications, and ticket creation
- **Key Concepts**: No-code agent configuration, API wrapping, webhook orchestration, low-code → production pipelines

### [Capstone Project: The Autonomous M&A Intelligence Swarm](./Capstone_Project/)
Synthesizes all 5 frameworks into a single end-to-end pipeline for **Venture Capital Investment Analysis**:
1. **Ingestion Phase** (LangChain RAG): Pitch deck parsing + vector indexing
2. **Research Phase** (smolagents): Competitive landscape web research
3. **Debate Phase** (AutoGen): Investment committee agents argue Bull vs. Bear thesis
4. **Synthesis Phase** (CrewAI): Structured investment memo generation
5. **Delivery Phase** (Dify): REST API packaging for portfolio management systems

---

## ⚡ Interactive Learning Environment

Every chapter includes a **Premium Interactive Notebook** with four hallmark features:

| Feature | Details |
|---------|---------|
| **Visual UI Contexts** | Custom high-fidelity UIs rendered in-notebook — Brutalist, Glassmorphism, and Dark Mode terminal aesthetics |
| **Cost Optimized** | All notebooks default to `gpt-4o-mini` (≈$0.15/1M tokens) — a full chapter costs less than $0.01 |
| **Hybrid Simulation Mode** | No API keys required — every notebook ships with a high-fidelity simulation so you can observe agentic behavior immediately |
| **Silent Execution** | `%%capture` magic suppresses framework noise; output is rendered exclusively via clean HTML/CSS UIs |

---

## 📁 Notebooks at a Glance

| Chapter | Notebook | Business Problem | Agents / Nodes | Framework |
|---------|----------|-----------------|----------------|-----------|
| Ch1 | AutoGen Boardroom | Financial Q3 Report | 5 agents | AutoGen |
| Ch1 | Semantic Kernel | Brand Compliance | 1 plugin chain | Semantic Kernel |
| Ch2 | LangChain RAG | HR Policy Retrieval | 7-section handbook | LangChain + ChromaDB |
| Ch2 | LangGraph Router | Support Ticket Routing | 7 nodes | LangGraph |
| Ch3 | OpenAI Assistants | Legal Contract Audit | 3 clauses | OpenAI API |
| Ch3 | Google ADK | PropTech Investment | 3 markets | Google ADK |
| Ch4 | CrewAI Swarm | Marketing Campaign | 4 agents | CrewAI |
| Ch4 | smolagents | Tax Discrepancy Audit | 5 transactions | smolagents |
| Ch5 | Dify | Sales Concierge | REST API | Dify |
| Ch5 | n8n | VIP Escalation | Webhook workflow | n8n |

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone <repo-url>
cd AI-Agent-Masterclass
```

### 2. Configure Environment Variables
```bash
cp .env.example .env
```
Open `.env` and add your keys:
```env
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...
LANGCHAIN_API_KEY=...          # Optional — for LangSmith tracing
TAVILY_API_KEY=...             # Optional — for web search in smolagents
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Launch JupyterLab
```bash
jupyter lab
```
Open any notebook in `Code_Examples/` to begin. Start with `Chapter_1` if you're new to multi-agent systems.

### Docker (Optional)
A `Dockerfile` is provided for containerized execution:
```bash
docker build -t ai-agent-course .
docker run -p 8888:8888 ai-agent-course
```

---

## 📦 Technology Stack

| Category | Package | Version |
|----------|---------|---------|
| Microsoft Agents | `pyautogen` | 0.2.14 |
| Microsoft Kernel | `semantic-kernel` | 0.9.1 |
| LangChain Core | `langchain` | 0.1.13 |
| LangChain Community | `langchain-community` | 0.0.29 |
| LangChain OpenAI | `langchain-openai` | 0.0.8 |
| Graph Orchestration | `langgraph` | 0.0.26 |
| Vector Store | `chromadb` | 0.4.24 |
| OpenAI SDK | `openai` | 1.14.2 |
| Google AI Platform | `google-cloud-aiplatform` | 1.44.0 |
| Agent Crews | `crewai` | 0.22.4 |
| HuggingFace Agents | `smolagents` | 0.0.1 |
| Notebook Runtime | `jupyterlab` | 4.1.5 |
| Observability | `langsmith` | 0.1.31 |
| Environment | `python-dotenv` | 1.0.1 |

---

## 🗺️ Learning Path

```
Chapter 1 (AutoGen + SK)
    ↓  multi-agent chat fundamentals
Chapter 2 (LangChain + LangGraph)
    ↓  RAG pipelines + stateful graphs
Chapter 3 (OpenAI + Google ADK)
    ↓  native provider tooling + structured output
Chapter 4 (CrewAI + smolagents)
    ↓  specialized open-source + ReAct loops
Chapter 5 (Dify + n8n)
    ↓  enterprise low-code deployment
Capstone (All Frameworks)
    → Full M&A Intelligence Swarm
```

---

## 📖 Additional Resources

| Resource | Description |
|----------|-------------|
| [`AI_Agent_Course.md`](./AI_Agent_Course.md) | Full course outline with learning objectives per chapter |
| [`AI_Agent_Course.pdf`](./AI_Agent_Course.pdf) | Printable PDF version of the complete course |
| [`Chapter_6_Observability_and_Tracing.md`](./Chapter_6_Observability_and_Tracing.md) | Bonus chapter: LangSmith tracing, debugging, and production monitoring |

---

## 🔑 API Key Requirements by Chapter

| Chapter | Required | Optional |
|---------|---------|---------|
| Ch1 — AutoGen / SK | `OPENAI_API_KEY` | — |
| Ch2 — LangChain / LangGraph | `OPENAI_API_KEY` | `LANGCHAIN_API_KEY` (tracing) |
| Ch3 — OpenAI Assistants | `OPENAI_API_KEY` | — |
| Ch3 — Google ADK | `GOOGLE_API_KEY` | — |
| Ch4 — CrewAI | `OPENAI_API_KEY` | `TAVILY_API_KEY` (web search) |
| Ch4 — smolagents | `OPENAI_API_KEY` | `TAVILY_API_KEY` |
| Ch5 — Dify / n8n | Platform credentials | — |
| All | — | `LANGCHAIN_API_KEY` (LangSmith) |

> All chapters support **simulation mode** — set `SIMULATION_MODE=true` in your `.env` to run without any API keys.

---

*Created by Umang (Senior Data Scientist) & Antigravity (Advanced Agentic AI Assistant).*
