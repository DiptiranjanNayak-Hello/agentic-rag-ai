# from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from app.core.llm import llm
from app.agents.tools import tools

from app.memory.manager import checkpointer

# memory = MemorySaver()

SYSTEM_PROMPT = """
You are a helpful AI agent with access to a specialized PDF knowledge base.
- If the user asks about the documents, use the 'query_knowledge_base' tool.
- If the user returns no relevant information, tell the user honestly.
- Always cite the Source and Page number provided in the tool output.
- Be concise and professional.
"""

agent_executor = create_react_agent(
    llm, 
    tools, 
    prompt=SYSTEM_PROMPT,
    # checkpointer=memory
    checkpointer=checkpointer
)
