# Capstone Project: The Autonomous M&A Intelligence Swarm 💎🚀

Welcome to the graduation challenge. In this project, you will build a industry-disrupting system: **The Autonomous Venture Capital Analyst.**

## 🏢 The Business Problem
Venture Capitalists and M&A (Mergers & Acquisitions) firms spend thousands of hours manually reviewing startup pitch decks, researching hidden competitors, and debating the "Go/No-Go" decision in smoke-filled boardrooms. 

**Your Goal:** Replace this manual labor with an autonomous swarm that conducts a full 360-degree investment audit in under 60 seconds.

---

## 🏗️ The Multi-Framework Architecture
To solve this, you must integrate the best features of every framework we've learned:

### Phase 1: The Pitch Deck Ingest (LangChain)
*   **The Problem**: Reading a 30-page PDF pitch deck is slow.
*   **The Solution**: Use a **LangChain RAG pipeline** to ingest the deck and extract the Core Value Proposition, Founders' Background, and Financial Asks.

### Phase 2: The Competitive Shadow Research (CrewAI)
*   **The Problem**: Pitch decks always hide the competition.
*   **The Solution**: Spin up a **CrewAI Swarm** (Researcher + Analyst). They will use the search tool to find "The Hidden Competitors" that the founders didn't mention.

### Phase 3: The Investment Committee Debate (AutoGen)
*   **The Problem**: One AI's opinion is biased.
*   **The Solution**: Create an **AutoGen Group Chat** featuring two personas:
    1.  **The Bull (Aggressive Optimist)**: Highlighting the upside and market potential.
    2.  **The Bear (Strict Auditor)**: Identifying legal risks and technical debt.
*   Let them debate for 3 turns until a consensus is reached.

### Phase 4: Final Investment Thesis (UI)
*   Render a **Premium Investment Thesis** (Markdown/HTML) that includes:
    *   Verified Financials (via smolagents).
    *   Market Risk Score.
    *   The "Deal Recommendation."

---

## 🛠️ Implementation Guide
1. Open [`main_orchestrator.ipynb`](./main_orchestrator.ipynb).
2. Follow the multi-framework integration guide.
3. Deploy your "VC Agent" as a headless service using a Dify API Bridge.

---
*Good luck. The future of autonomous finance is in your hands.*
