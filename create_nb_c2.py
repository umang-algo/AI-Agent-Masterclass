"""
create_nb_c2.py
---------------
Regenerates Chapter 2 notebooks for the AI Agent SDK Course.
Run: python create_nb_c2.py
"""
import json
import os

NOTEBOOKS_DIR = os.path.join(os.path.dirname(__file__), "Code_Examples")
os.makedirs(NOTEBOOKS_DIR, exist_ok=True)

# ─────────────────────────────────────────────────────────────────────────────
# NOTEBOOK 1: Chapter2_LangGraph_Support.ipynb
# ─────────────────────────────────────────────────────────────────────────────

langgraph_code = """\
import os
import sys
from typing import TypedDict, Literal

# Install dependencies
!{sys.executable} -m pip install --quiet langchain langchain_openai langgraph

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from IPython.display import display, HTML

# ── 1. API Key ────────────────────────────────────────────────────────────────
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# ── 2. Define the shared state passed between every graph node ────────────────
class SupportState(TypedDict):
    ticket_text: str
    intent: str
    response: str
    actions: list
    log: list

llm = ChatOpenAI(model="gpt-4-turbo")

# ── 3. Node: Intent Classifier ───────────────────────────────────────────────
def classify_intent_node(state: SupportState):
    prompt = (
        f"You are a customer support triage system. "
        f"Determine the intent of this ticket: '{state['ticket_text']}'. "
        f"Output EXACTLY one word — either 'refund' or 'technical'."
    )
    try:
        result = llm.invoke(prompt).content.strip().lower()
        intent = "refund" if "refund" in result else "technical"
    except Exception:
        intent = "refund"
    msg = f"🔍 Ticket received. Intent classified as **{intent.upper()}**."
    return {
        "intent": intent,
        "actions": ["classified"],
        "log": state["log"] + [{"sender": "Intent_Classifier", "msg": msg}]
    }

# ── 4. Node: Refund Agent ────────────────────────────────────────────────────
def refund_agent_node(state: SupportState):
    response = (
        "✅ Refund approved! I have initiated a full refund to your original payment method. "
        "You should see the credit within 3–5 business days. "
        "A confirmation email has been dispatched to the address on file."
    )
    return {
        "response": response,
        "actions": state["actions"] + ["refunded"],
        "log": state["log"] + [{"sender": "Refund_Agent", "msg": response}]
    }

# ── 5. Node: Technical Support Agent ────────────────────────────────────────
def technical_agent_node(state: SupportState):
    prompt = (
        f"You are a senior technical support engineer. "
        f"Draft a polite, professional troubleshooting email for: '{state['ticket_text']}'. "
        f"Keep it under 80 words and include a concrete first step."
    )
    try:
        response = llm.invoke(prompt).content
    except Exception:
        response = (
            "📧 Hi there! Thank you for reaching out. "
            "Please try clearing your browser cache and restarting the app. "
            "If the issue persists, reply with your OS version. — Support Team"
        )
    return {
        "response": response,
        "actions": state["actions"] + ["drafted_email"],
        "log": state["log"] + [{"sender": "Technical_Agent", "msg": response}]
    }

# ── 6. Routing Edge ──────────────────────────────────────────────────────────
def route_ticket(state: SupportState) -> Literal["refund_agent", "technical_agent"]:
    return "refund_agent" if state["intent"] == "refund" else "technical_agent"

# ── 7. Compile the Graph ─────────────────────────────────────────────────────
workflow = StateGraph(SupportState)
workflow.add_node("classifier", classify_intent_node)
workflow.add_node("refund_agent", refund_agent_node)
workflow.add_node("technical_agent", technical_agent_node)
workflow.set_entry_point("classifier")
workflow.add_conditional_edges("classifier", route_ticket)
workflow.add_edge("refund_agent", END)
workflow.add_edge("technical_agent", END)
app = workflow.compile()

# ── 8. UI Renderer ────────────────────────────────────────────────────────────
def render_support_chat(log: list, ticket: str):
    html = '''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        .sc-wrap { max-width: 820px; margin: 24px auto; font-family: 'Inter', sans-serif; background: #0f0f1a; padding: 32px; border-radius: 24px; box-shadow: 0 24px 60px rgba(0,0,0,0.6); border: 1px solid #1e1e3a; }
        .sc-title { text-align:center; font-size: 22px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 8px; background: linear-gradient(90deg, #a78bfa, #60a5fa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .sc-subtitle { text-align:center; font-size: 13px; color: #555; margin-bottom: 28px; }
        .sc-ticket { background: #1a1a2e; border-left: 4px solid #6366f1; padding: 16px 20px; border-radius: 12px; color: #d1d5db; font-size: 14px; margin-bottom: 24px; line-height: 1.6; }
        .sc-ticket strong { color: #a78bfa; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; display: block; margin-bottom: 6px; }
        .sc-bubble { padding: 16px 22px; margin: 16px 0; border-radius: 18px; max-width: 85%; font-size: 14px; line-height: 1.7; color: #fff; box-shadow: 0 6px 20px rgba(0,0,0,0.2); }
        .sc-name { font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px; }
        .Intent_Classifier { background: linear-gradient(135deg, #7c3aed, #4f46e5); margin-right: auto; border-bottom-left-radius: 4px; }
        .Refund_Agent      { background: linear-gradient(135deg, #059669, #10b981); margin-right: auto; border-bottom-left-radius: 4px; }
        .Technical_Agent   { background: linear-gradient(135deg, #d97706, #f59e0b); margin-right: auto; border-bottom-left-radius: 4px; color: #0a0a0a !important; }
    </style>
    <div class="sc-wrap">
        <div class="sc-title">⚡ LangGraph Support Router</div>
        <div class="sc-subtitle">Deterministic State-Machine Routing — Chapter 2 Demo</div>
    '''
    html += f'<div class="sc-ticket"><strong>📨 Incoming Ticket</strong>{ticket}</div>'
    icons = {"Intent_Classifier": "🤖", "Refund_Agent": "💳", "Technical_Agent": "🛠"}
    for entry in log:
        s = entry.get("sender", "System")
        sc = s.replace(" ", "_")
        icon = icons.get(sc, "💬")
        html += f'<div class="sc-bubble {sc}"><div class="sc-name">{icon} {s.replace("_"," ")}</div><div>{entry.get("msg","")}</div></div>'
    html += '</div>'
    display(HTML(html))

# ── 9. Run Two Example Tickets ───────────────────────────────────────────────
tickets = [
    "I was charged twice for my subscription last month and want my money back immediately.",
    "The app keeps crashing every time I try to export a PDF report on Windows 11."
]

for ticket in tickets:
    try:
        result = app.invoke({
            "ticket_text": ticket, "intent": "",
            "response": "", "actions": [], "log": []
        })
        render_support_chat(result["log"], ticket)
    except Exception as e:
        print(f"Error: {e}")
"""

nb_langgraph = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Interactive Agent Session: Chapter 2 — LangGraph Customer Support Router\n\n",
                "This Jupyter notebook demonstrates **LangGraph** deterministically routing customer support tickets through a strict state-machine graph.\n\n",
                "**Prerequisites:** Set your `OPENAI_API_KEY` inside the code cell below. The notebook gracefully falls back to simulated responses if no key is provided."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [line + "\n" for line in langgraph_code.split("\n")]
        }
    ],
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.11"}
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# ─────────────────────────────────────────────────────────────────────────────
# NOTEBOOK 2: Chapter2_LangChain_HR_RAG.ipynb
# ─────────────────────────────────────────────────────────────────────────────

langchain_code = """\
import os
import sys

# Install dependencies
!{sys.executable} -m pip install --quiet langchain langchain_openai langchain_community langchain_chroma chromadb

from langchain.schema import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from IPython.display import display, HTML

# ── 1. API Key ────────────────────────────────────────────────────────────────
# os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"

# ── 2. Simulated HR Policy Knowledge Base ────────────────────────────────────
HR_POLICY_TEXT = \"\"\"
SECTION 1: PAID TIME OFF (PTO)
Full-time employees accrue 20 days of paid time off (PTO) per calendar year at a rate of 1.67 days/month.
Unused PTO may be carried over up to 10 days. Requests must be submitted 2 weeks in advance via HR portal.

SECTION 2: PARENTAL LEAVE
The company provides 16 weeks of fully paid maternity leave and 4 weeks of fully paid paternity leave.
Eligibility requires 12 months of continuous full-time employment. Adoptive parents receive equal benefits.

SECTION 3: HEALTH INSURANCE
The company covers 90% of the employee premium. Dental and vision are included at no extra cost.
Dependents may be added; the company contributes 60% of dependent premiums. Open enrollment is in November.

SECTION 4: REMOTE WORK POLICY
Employees may work remotely up to 3 days per week with manager approval. Core hours: 10 AM–3 PM local time.
A $600/year home office setup stipend is provided.

SECTION 5: PERFORMANCE REVIEWS
Reviews are conducted twice per year (June and December). Compensation adjustments are tied to the December cycle.
Two consecutive 'Exceeds Expectations' ratings qualify employees for automatic promotion consideration.

SECTION 6: PROFESSIONAL DEVELOPMENT
Each employee receives a $2,000 annual learning budget for courses, certifications, conferences, and books.
10 paid study days per year are available for employees pursuing industry certifications.

SECTION 7: GRIEVANCE & COMPLAINT PROCESS
Formal complaints must be submitted in writing to HR within 30 days of the incident.
HR acknowledges receipt within 48 hours and initiates investigation within 5 business days.
Retaliation against employees raising grievances is a terminable offense.
\"\"\"

# ── 3. Split and vectorize ────────────────────────────────────────────────────
splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)
raw_docs = [Document(page_content=HR_POLICY_TEXT, metadata={"source": "employee_handbook_v3.pdf"})]
chunks = splitter.split_documents(raw_docs)
print(f"📚 Knowledge base split into {len(chunks)} retrievable chunks.")

try:
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    USE_REAL_LLM = True
    print("✅ Vector store built. LLM mode active.")
except Exception as e:
    USE_REAL_LLM = False
    print(f"⚠️  Demo mode active (no API key). ({e})")

# ── 4. RAG Chain ──────────────────────────────────────────────────────────────
SIMULATED_ANSWERS = {
    0: "You are entitled to **4 weeks (20 business days)** of fully paid paternity leave. Requires 12 months of continuous employment.",
    1: "You may work remotely up to **3 days per week** with manager approval. Core hours: 10 AM–3 PM. You receive a **$600/year** home office stipend.",
    2: "Your annual learning budget is **$2,000** covering courses, certifications, conferences, and books, plus **10 paid study days** per year."
}

if USE_REAL_LLM:
    llm = ChatOpenAI(model="gpt-4-turbo")
    system_prompt = (
        "You are an authoritative HR Assistant. Answer questions strictly based on the HR policy context below. "
        "If the answer is not in the context, say 'I could not find that information in the current policy handbook.'\\n\\nContext:\\n{context}"
    )
    prompt_template = ChatPromptTemplate.from_messages([("system", system_prompt), ("human", "{input}")])
    rag_chain = create_retrieval_chain(retriever, create_stuff_documents_chain(llm, prompt_template))

# ── 5. UI Renderer ────────────────────────────────────────────────────────────
def render_rag_ui(qa_pairs: list):
    html = '''
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        .rag-wrap { max-width: 820px; margin: 24px auto; font-family: 'Inter', sans-serif; background: #0f0f1a; padding: 32px; border-radius: 24px; box-shadow: 0 24px 60px rgba(0,0,0,0.6); border: 1px solid #1e1e3a; }
        .rag-title { text-align:center; font-size: 22px; font-weight: 800; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 6px; background: linear-gradient(90deg, #f472b6, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .rag-sub { text-align:center; color: #555; font-size: 13px; margin-bottom: 28px; }
        .rag-card { background: #131320; border: 1px solid #1e1e3a; border-radius: 18px; padding: 22px 26px; margin: 18px 0; }
        .rag-q { font-size: 13px; font-weight: 800; color: #818cf8; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 10px; }
        .rag-q-text { font-size: 15px; color: #e2e8f0; font-weight: 600; border-left: 3px solid #6366f1; padding-left: 14px; margin: 0 0 16px 0; line-height: 1.6; }
        .rag-a-label { font-size: 11px; font-weight: 800; color: #34d399; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px; }
        .rag-a-text { background: linear-gradient(135deg, #064e3b, #065f46); border: 1px solid #059669; border-radius: 12px; padding: 14px 18px; color: #d1fae5; font-size: 14px; line-height: 1.7; }
        .rag-src { margin-top: 12px; font-size: 11px; color: #4b5563; }
    </style>
    <div class="rag-wrap">
        <div class="rag-title">📋 HR Policy Q&A Assistant</div>
        <div class="rag-sub">LangChain RAG Pipeline · Retrieval-Augmented Generation Demo</div>
    '''
    for i, pair in enumerate(qa_pairs):
        html += f'''
        <div class="rag-card">
            <div class="rag-q">🙋 Question {i+1}</div>
            <div class="rag-q-text">{pair["question"]}</div>
            <div class="rag-a-label">✅ HR Assistant Response</div>
            <div class="rag-a-text">{pair["answer"]}</div>
            <div class="rag-src">📄 Source: employee_handbook_v3.pdf · Retrieved {pair["chunks"]} policy chunks</div>
        </div>'''
    html += '</div>'
    display(HTML(html))

# ── 6. Run Questions ──────────────────────────────────────────────────────────
questions = [
    "How many days of paid paternity leave am I entitled to?",
    "What is the remote work policy — how many days can I work from home?",
    "What is my annual budget for professional development and certifications?"
]

results = []
for i, question in enumerate(questions):
    try:
        if USE_REAL_LLM:
            resp = rag_chain.invoke({"input": question})
            answer = resp["answer"]
            num_chunks = len(resp.get("context", []))
        else:
            answer = SIMULATED_ANSWERS.get(i, "Simulated answer not available.")
            num_chunks = 3
        results.append({"question": question, "answer": answer, "chunks": num_chunks})
    except Exception as e:
        results.append({"question": question, "answer": f"Error: {e}", "chunks": 0})

render_rag_ui(results)
"""

nb_langchain = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Interactive Agent Session: Chapter 2 — LangChain HR Document Q&A (RAG)\n\n",
                "This Jupyter notebook demonstrates a **Retrieval-Augmented Generation (RAG)** pipeline using LangChain with a built-in simulated HR policy knowledge base — no PDF file required!\n\n",
                "**Prerequisites:** Set your `OPENAI_API_KEY` inside the code cell. The notebook gracefully falls back to demo mode if no key is provided."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [line + "\n" for line in langchain_code.split("\n")]
        }
    ],
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.11"}
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

# ─────────────────────────────────────────────────────────────────────────────
# Write both notebooks
# ─────────────────────────────────────────────────────────────────────────────

nb1_path = os.path.join(NOTEBOOKS_DIR, "Chapter2_LangGraph_Support.ipynb")
nb2_path = os.path.join(NOTEBOOKS_DIR, "Chapter2_LangChain_HR_RAG.ipynb")

with open(nb1_path, "w") as f:
    json.dump(nb_langgraph, f, indent=2)
print(f"✅ Created: {nb1_path}")

with open(nb2_path, "w") as f:
    json.dump(nb_langchain, f, indent=2)
print(f"✅ Created: {nb2_path}")
