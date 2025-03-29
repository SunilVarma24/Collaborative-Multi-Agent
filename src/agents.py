# src/agents.py
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import BaseMessage, ToolMessage, AIMessage

from src.tools import tv_search, python_repl

# Initialize LLM
llm = ChatOpenAI(model="gpt-4o", temperature=0)

# Create Research Agent
search_tool = [tv_search]
search_tool_name = tv_search.name
research_prompt = ChatPromptTemplate.from_messages([
    ("system", f"""You are a helpful AI assistant, collaborating with other assistants.
Use the provided tools to progress towards answering the question.
If you are unable to fully answer, that's OK,
another assistant with different tools will help where you left off.
Execute what you can to make progress.
If you or any of the other assistants have the final answer or deliverable,
prefix your response with FINAL ANSWER so the team knows to stop.

You have access to the following tools:
{search_tool_name}

You should provide accurate data for use
and source code shouldn't be the final answer
"""),
    MessagesPlaceholder(variable_name="messages"),
])
research_agent = research_prompt | llm.bind_tools(search_tool)

# Create Chart Agent
chart_tool = [python_repl]
chart_tool_name = python_repl.name
chart_prompt = ChatPromptTemplate.from_messages([
    ("system", f"""You are a helpful AI assistant, collaborating with other assistants.
Use the provided tools to progress towards answering the question.
If you are unable to fully answer, that's OK,
another assistant with different tools will help where you left off.
Execute what you can to make progress.
If you or any of the other assistants have the final answer or deliverable,
prefix your response with FINAL ANSWER so the team knows to stop.

You have access to the following tools:
{chart_tool_name}

Run the python code to display the chart
"""),
    MessagesPlaceholder(variable_name="messages"),
])
chart_agent = chart_prompt | llm.bind_tools(chart_tool)

# Define Agent Nodes
def research_agent_node(state):
    result = research_agent.invoke(state)
    if isinstance(result, ToolMessage):
        pass
    else:
        result = AIMessage(**result.dict(exclude={"type", "name"}), name="Researcher")
    return {"messages": [result], "sender": "Researcher"}

def chart_agent_node(state):
    result = chart_agent.invoke(state)
    if isinstance(result, ToolMessage):
        pass
    else:
        result = AIMessage(**result.dict(exclude={"type", "name"}), name="chart_generator")
    return {"messages": [result], "sender": "chart_generator"}
