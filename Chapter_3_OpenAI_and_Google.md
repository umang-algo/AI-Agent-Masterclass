# Chapter 3: Native Provider Tooling (OpenAI & Google) ☁️

Why use a third-party framework when the model providers themselves offer native Agent SDKs? In this chapter, we explore specialized tools from the giants of AI.

## 1. Google Gen AI SDK (Agent Development Kit) 🔎
### The Business Problem:
Real estate investors rely on outdated broker reports and gut feelings. A single bad investment in the wrong neighborhood can lose $500K. They need factually grounded, real-time market intelligence — not AI hallucinations.

### The SDK Solution:
Google's **Agent Development Kit** integrates with Gemini 2.0 and provides native **Search Grounding** — the model verifies every claim against live Google Search results before responding.

### 🧩 Business Case: Multi-Market PropTech Investment Auditor
*   **The Problem**: Comparing 3 real estate markets with different strategies to find the best risk-adjusted investment.
*   **The Result**: A comprehensive audit of 3 markets with buy/hold/sell verdicts.

**Markets Audited:**

| Market | Budget | Strategy | Verdict |
|--------|--------|----------|---------|
| Silver Lake, Los Angeles | $1.5M | Long-term rental | **BUY** — Strong appreciation |
| Austin, Texas (East Side) | $600K | Airbnb / Short-term | **HOLD** — STR permit risk |
| Miami Beach, Florida | $2.2M | Luxury flip | **BUY** — Luxury segment resilient |

*   **Technical Highlights**:
    *   `google_search_retrieval` tool for live fact verification
    *   Gemini 2.0 Flash for cost-efficient analysis
    *   Luxury editorial UI (Playfair Display typography)

---

## 2. OpenAI Assistants API (Assistants SDK) 🦾
### The Business Problem:
Legal teams manually review 100+ page vendor contracts. A single missed liability clause can cost millions. The audit must track changes across multiple sessions without losing context.

### The SDK Solution:
OpenAI's **Assistants API** stores the conversation (Threads) on their servers, enabling truly **Stateful** multi-turn audits without managing chat history yourself.

### 🧩 Business Case: Multi-Clause Contract Risk Auditor
*   **The Problem**: Three dangerous contract clauses need professional risk assessment with specific legal citations.
*   **The Result**: A comprehensive audit with risk scoring across 3 clauses.

**Clauses Audited:**

| Clause | Title | Risk Level |
|--------|-------|------------|
| CL-14 | Limitation of Liability | 🔴 **CRITICAL** — Eliminates liability for gross negligence |
| CL-22 | Data Handling & Privacy | 🟠 **HIGH** — Violates GDPR Article 6 and CCPA |
| CL-31 | Termination & Exit | 🟡 **MEDIUM** — $50K exit fee creates vendor lock-in |

*   **Technical Highlights**:
    *   `client.beta.assistants.create()` for managed agent instances
    *   `client.beta.threads.runs.create_and_poll()` for async execution
    *   Risk color-coded UI with clause-by-clause breakdown

---

👉 **[Launch the Interactive Notebook: Chapter 3 Google ADK](./Code_Examples/Chapter3_GoogleADK_PropTech.ipynb)**
👉 **[Launch the Interactive Notebook: Chapter 3 OpenAI Legal](./Code_Examples/Chapter3_OpenAI_LegalAuditor.ipynb)**
