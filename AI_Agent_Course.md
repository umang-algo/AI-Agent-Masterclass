# AI Agent SDKs & Frameworks: The Master Course (2026 Edition) 🎓🚀

Welcome to the definitive guide on **AI Agent SDKs and Frameworks**. This course is designed to transition you from "Chatting with AI" to **"Orchestrating Autonomous Business Systems."**

---

## 🏛️ Course Overview: The Age of Orchestration
The primary problem in modern software is no longer "Intelligence"—it is **Orchestration.** 

If you ask a raw LLM to conduct a legal audit or a financial tax summary, it will likely hallucinate mathematical results or miss critical context. To solve this, we use **Agent Frameworks.** 

In this course, we explore the major SDKs, solve **real-world industry problems** in Marketing, Finance, Legal, HR, and Real Estate, provide **interactive premium notebooks**, and evaluate the strengths of each framework.

---

## 🏗️ Chapter 1: The Microsoft Ecosystem
Microsoft caters to enterprise collaboration and deep architectural integration.

### 1. AutoGen: The Collaborative Swarm 🐝
*   **The Business Problem**: A Q3 investment report for MSFT and TSLA requires data fetching, analysis, QA testing, and risk scoring — typically 4 different roles.
*   **The SDK Solution**: AutoGen creates a 5-agent boardroom (CEO, Data Engineer, Analyst, QA Tester, Risk Manager) that autonomously debates and produces a verified report.
*   **Key Features**: `GroupChat` orchestration, `%%capture` silent execution, live `yfinance` data, premium boardroom UI
*   📁 **Code**: [`Chapter1_AutoGen_Company.ipynb`](./Code_Examples/Chapter1_AutoGen_Company.ipynb)

### 2. Semantic Kernel: Enterprise AI Glue 🏗️
*   **The Business Problem**: Raw LLM output must pass through brand rules (title case, 120-char limit, legal footer) before publication.
*   **The SDK Solution**: Semantic Kernel wraps Python business logic as reusable **Native Plugins** via `@kernel_function`.
*   **Key Features**: `BrandCompliancePlugin`, `ChatHistory` with strict prompts, green-on-black terminal UI
*   📁 **Code**: [`Chapter1_SemanticKernel_Marketing.ipynb`](./Code_Examples/Chapter1_SemanticKernel_Marketing.ipynb)

---

## 🕸️ Chapter 2: The LangChain Ecosystem
The industry standard for document intelligence and stateful logic.

### 1. LangChain: Retrieval-Augmented Generation (RAG) 📚
*   **The Business Problem**: HR teams answer the same 50 questions daily. Employees wait hours for PTO, parental leave, and benefits answers.
*   **The SDK Solution**: A full RAG pipeline: 7-section HR Handbook → RecursiveCharacterTextSplitter → OpenAI Embeddings → ChromaDB → Retrieval Chain.
*   **Key Features**: 7 policy sections, 4 employee queries, Policy ID citations, dark-mode chat UI
*   📁 **Code**: [`Chapter2_LangChain_HR_RAG.ipynb`](./Code_Examples/Chapter2_LangChain_HR_RAG.ipynb)

### 2. LangGraph: Deterministic State Machines 🤖
*   **The Business Problem**: Support tickets misrouted 40% of the time. No sentiment awareness. VIPs treated same as standard users.
*   **The SDK Solution**: A 7-node LangGraph state machine: Sentiment → Classifier → Priority → Handler → Escalation.
*   **Key Features**: 4 intent types (refund/billing/technical/account), VIP detection, P0-P3 priority scoring, 3 test tickets
*   📁 **Code**: [`Chapter2_LangGraph_Support.ipynb`](./Code_Examples/Chapter2_LangGraph_Support.ipynb)

---

## ☁️ Chapter 3: Native Provider Tooling (Google & OpenAI)
Highly optimized agent SDKs built directly by the model creators.

### 1. Google Gen AI SDK (Agent Development Kit) 🔎
*   **The Business Problem**: Real estate investors need factually grounded market intelligence across multiple markets — not AI hallucinations.
*   **The SDK Solution**: Gemini 2.0 with **Search Grounding** — verifies every claim against live Google Search results.
*   **Key Features**: 3-market comparison (Silver Lake / Austin / Miami), buy/hold/sell verdicts, luxury editorial UI
*   📁 **Code**: [`Chapter3_GoogleADK_PropTech.ipynb`](./Code_Examples/Chapter3_GoogleADK_PropTech.ipynb)

### 2. OpenAI Assistants SDK 🦾
*   **The Business Problem**: Legal teams manually review vendor contracts. A missed liability clause can cost millions in litigation.
*   **The SDK Solution**: Assistants API with **Stateful Threads** — audits 3 contract clauses with CRITICAL/HIGH/MEDIUM risk scoring.
*   **Key Features**: 3-clause audit (Liability, Privacy, Termination), GDPR/CCPA citations, risk-colored legal report UI
*   📁 **Code**: [`Chapter3_OpenAI_LegalAuditor.ipynb`](./Code_Examples/Chapter3_OpenAI_LegalAuditor.ipynb)

---

## 🧪 Chapter 4: Specialized Open-Source
Frameworks that solve role-playing and code-generation paradigms.

### 1. CrewAI: Role-Playing Collaboration 👥
*   **The Business Problem**: 360° marketing campaigns require 4 different hires: researcher, strategist, copywriter, and brand reviewer.
*   **The SDK Solution**: CrewAI orchestrates a 4-agent sequential pipeline where each agent builds on the previous output.
*   **Key Features**: Rich agent backstories, FTC compliance review, 4-panel strategy deck UI
*   📁 **Code**: [`Chapter4_CrewAI_Marketing.ipynb`](./Code_Examples/Chapter4_CrewAI_Marketing.ipynb)

### 2. HuggingFace smolagents: Code-Native Execution 🧮
*   **The Business Problem**: LLMs hallucinate numbers. Tax audits across UK, US, and EU require 100% mathematical precision.
*   **The SDK Solution**: smolagents writes and executes Python code autonomously — 5 transactions, 2 discrepancies detected ($285 total).
*   **Key Features**: Multi-region tax audit table, PASS/DISCREPANCY flags, deterministic Python execution
*   📁 **Code**: [`Chapter4_SmolAgents_TaxAuditor.ipynb`](./Code_Examples/Chapter4_SmolAgents_TaxAuditor.ipynb)

---

## ⚡ Chapter 5: Enterprise Low-Code Platforms
Scaling AI through orchestration platforms.

### 1. Dify: The Headless Agent Engine 🤖
*   **The Business Case**: **Headless Sales Concierge.** Decouple agent logic from Python code so PMs can update the bot visually in Dify while engineers consume it as a REST API.
*   **Key Features**: Stateful `conversation_id` tracking, blocking response mode, Enterprise tier pricing intelligence
*   📁 **Code**: [`Chapter5_Dify_HeadlessAPI.ipynb`](./Code_Examples/Chapter5_Dify_HeadlessAPI.ipynb)

### 2. n8n: The Autonomous Action Layer ⚙️
*   **The Business Case**: **VIP Incident Escalation.** When a P0 VIP outage is detected, the agent fires a webhook to n8n triggering Slack alerts + CRM updates + priority support tickets.
*   **Key Features**: JSON webhook payloads, P0_EMERGENCY priority detection, multi-app orchestration across 500+ integrations
*   📁 **Code**: [`Chapter5_n8n_ActionOrchestrator.ipynb`](./Code_Examples/Chapter5_n8n_ActionOrchestrator.ipynb)

---

## 🔬 Chapter 6: Observability (Production Guardrails)
Building an agent is easy; knowing *why* it failed is hard.

### The "Black Box" Problem
In production, you need **Tracing**. Tools like **LangSmith** and **Arize Phoenix** act as the "Datadog" of AI, giving you a waterfall view of every tool call, token count, and latency spike.

---

## ⚡ Interactive Learning Environment
Every chapter includes a **Premium Interactive Notebook** that you can run locally:
*   **Visual UI Contexts**: Every agent demo features a custom-designed, high-fidelity UI rendered directly in your notebook (dark terminals, editorial layouts, strategy decks).
*   **Cost & Speed Optimized**: All notebooks use `gpt-4o-mini` by default (0.15¢ per 1M tokens) to ensure your learning is virtually free.
*   **Hybrid Simulation Mode**: No API Keys? No problem. Every notebook features a high-fidelity simulation mode so you can see the agentic behavior regardless of your environment.
*   **Silent Execution**: `%%capture` magic hides all framework logs — output is rendered via premium HTML/CSS UIs only.

---
*Created by Umang (Senior Data Scientist) & Antigravity AI Assistant.*
