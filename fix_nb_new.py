import json
import os

file = "/Users/umang/Desktop/Umang/AI-Agent-SDK/Course/Code_Examples/Chapter1_AutoGen_Company.ipynb"
with open(file, "r") as f:
    nb = json.load(f)

new_autogen_code = """import autogen

llm_config = {"model": "gpt-4-turbo", "api_key": "YOUR_OPENAI_API_KEY"}

# 1. Human Proxy (Set to NEVER interrupt to prevent Jupyter from hanging)
user_proxy = autogen.UserProxyAgent(
    name="User_Proxy",
    system_message="Human administrator.",
    code_execution_config={"work_dir": "coding", "use_docker": False},
    human_input_mode="NEVER", 
    is_termination_msg=lambda x: x.get("content", "") and "TERMINATE" in x.get("content", "")
)

# 2. Company Employees
ceo = autogen.AssistantAgent(
    name="CEO",
    system_message="You are the CEO. You orchestrate the team. When the final executive summary is complete and approved by everyone, output the final report and append the word 'TERMINATE' to close the chat.",
    llm_config=llm_config,
)

data_eng = autogen.AssistantAgent(
    name="Data_Engineer",
    system_message="You are a Data Engineer. Write executable Python code (using yfinance) to fetch stock data for MSFT and TSLA. Wait for the User_Proxy to return the results. Fix bugs if they crash.",
    llm_config=llm_config,
)

analyst = autogen.AssistantAgent(
    name="Financial_Analyst",
    system_message="You are a Financial Analyst. Read the raw terminal data provided by the Data Engineer and write a detailed market analysis.",
    llm_config=llm_config,
)

qa_tester = autogen.AssistantAgent(
    name="QA_Tester",
    system_message="You are the QA Tester. Review the Financial Analyst's calculations. Explicitly tell them to rewrite if wrong. Do not accept until mathematically sound.",
    llm_config=llm_config,
)

risk_manager = autogen.AssistantAgent(
    name="Risk_Manager",
    system_message="You are the Chief Risk Officer. Review the report and append a final 'Risk Score' from 1-10.",
    llm_config=llm_config,
)

# 3. Virtual Office
groupchat = autogen.GroupChat(
    agents=[user_proxy, ceo, data_eng, analyst, qa_tester, risk_manager], 
    messages=[], 
    max_round=12
)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# 4. Start the business day
chat_result = user_proxy.initiate_chat(
    manager, 
    message="We need a comprehensive Q3 investment report for MSFT and TSLA. Fetch data, analyze it, rigorously test for errors, assign a risk score, and then TERMINATE."
)
"""

ui_code = """from IPython.display import display, HTML

# 5. Build a Sexy Interactive UI using the Chat History!
def render_beautiful_chat(chat_history):
    html_content = '''
    <style>
        .chat-container { max-width: 850px; margin: 20px auto; font-family: 'Inter', -apple-system, sans-serif; background: #1a1b26; padding: 30px; border-radius: 20px; box-shadow: 0 20px 40px rgba(0,0,0,0.4); border: 1px solid #2f334d; }
        .chat-header { text-align: center; color: #fff; font-size: 24px; margin-bottom: 30px; font-weight: 800; letter-spacing: 1px; text-transform: uppercase; background: -webkit-linear-gradient(#00d2ff, #3a7bd5); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .message-bubble { padding: 18px 24px; margin: 20px 0; border-radius: 18px; max-width: 82%; color: white; font-size: 15px; line-height: 1.6; box-shadow: 0 8px 16px rgba(0,0,0,0.15); transition: transform 0.2s; }
        .message-bubble:hover { transform: translateY(-2px); }
        
        /* Vibrant Agent Gradients */
        .User_Proxy { background: linear-gradient(135deg, #007aff, #0056b3); margin-left: auto; border-bottom-right-radius: 4px; border: 1px solid #0056b3; }
        .CEO { background: linear-gradient(135deg, #8e2de2, #4a00e0); margin-right: auto; border-bottom-left-radius: 4px; border: 1px solid #4a00e0; }
        .Data_Engineer { background: linear-gradient(135deg, #f12711, #f5af19); margin-right: auto; border-bottom-left-radius: 4px; border: 1px solid #f12711; }
        .Financial_Analyst { background: linear-gradient(135deg, #11998e, #38ef7d); margin-right: auto; border-bottom-left-radius: 4px; border: 1px solid #11998e; color: #0a0a0a !important; font-weight: 500; }
        .QA_Tester { background: linear-gradient(135deg, #ff416c, #ff4b2b); margin-right: auto; border-bottom-left-radius: 4px; border: 1px solid #ff416c; }
        .Risk_Manager { background: linear-gradient(135deg, #fc4a1a, #f7b733); margin-right: auto; border-bottom-left-radius: 4px; border: 1px solid #fc4a1a; }
        
        .sender-name { font-size: 12px; font-weight: 800; text-transform: uppercase; margin-bottom: 8px; opacity: 0.9; letter-spacing: 1px; display: flex; align-items: center; }
        .code-block { background: #000; padding: 10px; border-radius: 8px; font-family: monospace; font-size: 12px; color: #0f0; overflow-x: auto; margin-top: 10px; border: 1px solid #333; }
    </style>
    <div class="chat-container">
        <div class="chat-header">AI Company Boardroom</div>
    '''
    
    for msg in chat_history:
        sender = msg.get("name", "Unknown").replace(" ", "_")
        content = msg.get("content", "")
        if not content: continue
        
        content = str(content).replace("```python", "<div class='code-block'>").replace("```", "</div>").replace("\\n", "<br>")
            
        html_content += f'''
        <div class="message-bubble {sender}">
            <div class="sender-name">🤖 {sender}</div>
            <div>{content}</div>
        </div>
        '''
        
    html_content += '</div>'
    display(HTML(html_content))

try:
    messages = user_proxy.chat_messages[manager]
    render_beautiful_chat(messages)
except Exception as e:
    print("Could not load UI:", e)
"""

cells = nb.get("cells", [])
found = False

has_ui = any("render_beautiful_chat" in str(c.get("source", "")) for c in cells)

for block in cells:
    if block["cell_type"] == "code" and "import autogen" in str(block["source"]):
        block["source"] = [line + "\n" for line in new_autogen_code.split("\n")]
        found = True
        break

if not has_ui:
    ui_cell = {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in ui_code.split("\n")]
    }
    cells.append(ui_cell)

if found:
    with open(file, "w") as f:
        json.dump(nb, f, indent=2)
    print("Notebook perfectly updated! You can inspect it now.")
else:
    print("Could not find the autogen cell to replace.")
