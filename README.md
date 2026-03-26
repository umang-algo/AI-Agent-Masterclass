# AI Agent SDKs & Frameworks: The Master Course

Welcome to the definitive course on **AI Agent SDKs and Frameworks** (2024–2025 Edition). 

## Course Overview & Introduction

As Large Language Models (LLMs) have evolved, the focal point of AI development has shifted far beyond simple chat interfaces. The industry is rapidly moving toward building autonomous and semi-autonomous **Agents**. 

### What is an AI Agent?
An agent is an AI system that doesn't just "talk to you"—it acts on your behalf. Agents can formulate sub-plans, interact with tools (APIs, databases, web search), remember past context, self-reflect on errors, and collaborate with other agents to solve complex tasks.

### What Problem Are We Solving?
The primary problem in modern software is **Orchestration**. 
If you simply ask an LLM, "Analyze my database and tell me if we are profitable," the LLM will fail. It doesn't have the data, the code execution environment, or the memory to track a multi-step financial audit. 

To solve this, we use **Agent Frameworks**. These SDKs solve orchestration problems by:
1. Providing an environment where the LLM can write a SQL query.
2. Providing a sandbox where that SQL query is safely executed.
3. Looping the results of that query back to the LLM to analyze.
4. Returning a final formatted answer.

In this course, we will explore the major frameworks available, explicitly state the **Business Problem** they solve, fix the problem with **Code Solutions**, and break down the **Advantages and Disadvantages** of each SDK so you know exactly which tool to pick for your specific project.

---

## Course Syllabus

- **[Chapter 1: The Microsoft Ecosystem](./Chapter_1_Microsoft_Ecosystem.md)**
  Dive into *AutoGen* for multi-agent conversations, and *Semantic Kernel* for enterprise orchestration.

- **[Chapter 2: The LangChain Ecosystem](./Chapter_2_LangChain_Ecosystem.md)**
  Explore the industry-standard *LangChain* for document ingestion, and its powerful stateful graph sibling, *LangGraph*, ideal for deterministic workflows.

- **[Chapter 3: Native Provider Tooling (OpenAI & Google)](./Chapter_3_OpenAI_and_Google.md)**
  Learn about the highly optimized *OpenAI Agents SDK (Assistants API)* and Google's *Agent Development Kit (ADK)*.

- **[Chapter 4: Specialized Open-Source Frameworks](./Chapter_4_Specialized_Open_Source_Frameworks.md)**
  Discover a variety of independent frameworks solving specific problems, highlighted by *CrewAI* (role-playing teams) and *SmolAgents* (coding models).

- **[Chapter 5: Enterprise and Low-Code Platforms](./Chapter_5_Enterprise_and_Low_Code_Platforms.md)**
  Understand how non-technical and enterprise users deploy agents at scale using *Dify* and *n8n* via API integration.

Let's begin by diving into chapter 1!
