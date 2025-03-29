# src/graph.py
from langgraph.prebuilt import ToolNode
from langgraph.graph import END, StateGraph
from typing import Literal
from langchain_core.messages import BaseMessage, ToolMessage, AIMessage
from typing import Annotated, Sequence, TypedDict
import operator

from src.agents import research_agent_node, chart_agent_node
from src.tools import tv_search, python_repl

# Define the global AgentState type
class AgentState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], operator.add]
    sender: str

# Define Tool Node (combining both tools)
tools = [tv_search, python_repl]
tool_node = ToolNode(tools)

# Define router edge logic
def router(state) -> Literal["call_tool", "__end__", "continue"]:
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        return "call_tool"
    if "FINAL ANSWER" in last_message.content:
        return "__end__"
    return "continue"

# Build the multi-agent graph
agent = StateGraph(AgentState)
agent.add_node("Researcher", research_agent_node)
agent.add_node("chart_generator", chart_agent_node)
agent.add_node("call_tool", tool_node)

agent.add_conditional_edges(
    "Researcher",
    router,
    {"continue": "chart_generator", "call_tool": "call_tool", "__end__": END},
)
agent.add_conditional_edges(
    "chart_generator",
    router,
    {"continue": "Researcher", "call_tool": "call_tool", "__end__": END},
)
agent.add_conditional_edges(
    "call_tool",
    lambda state: state["sender"],
    {"Researcher": "Researcher", "chart_generator": "chart_generator"},
)
agent.set_entry_point("Researcher")
agent = agent.compile()

# For visualization in main.py
def get_agent_graph():
    return agent.get_graph()

def get_compiled_agent():
    return agent
