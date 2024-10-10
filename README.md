# Collaborative Multi-Agent System using Tavily Search, PythonREPL, and LangChain

## Project Overview
This project implements a Collaborative Multi-Agent System that automates research and data visualization tasks by creating a team of agents. The system consists of two main agents: 
- **Researcher Agent**: Uses the Tavily search tool to fetch relevant web data.
- **Chart Agent**: Uses the PythonREPL tool to generate visualizations from the research data.

The agents communicate with each other and are orchestrated by a ChatGPT-4o model, which manages the interaction. This system was built using LangChain for agent integration and LangGraph for structured workflows.

## Introduction
The Collaborative Multi-Agent System is designed to automate tasks that require both research and data visualization. The system leverages the Tavily search tool to gather web data and the PythonREPL tool to generate Python-based charts from the data. The agents are orchestrated by ChatGPT 4o Model, allowing them to work collaboratively. The system is built using LangChain and LangGraph, providing a scalable and modular framework for multi-agent communication and task execution.

## System Architecture
1. **Researcher Agent**: Uses Tavily search to gather information from the web based on user queries.
2. **Chart Agent**: Processes the data gathered by the Researcher Agent and generates a chart using PythonREPL.
3. **ChatGPT-4o Model**: Manages agent interactions and ensures that data flows between agents efficiently.
4. **LangChain & LangGraph**: Provide the underlying framework for building and managing the agent workflows.

### Workflow Example:
1. The user asks a question requiring data research and visualization.
2. The Researcher Agent uses Tavily search to collect data from the web.
3. The data is passed to the Chart Agent, which processes it and generates a visualization using PythonREPL.
4. The system returns the final answer along with the visualization to the user.

## Installation
To run this project, you will need Python 3.x installed along with the following libraries:

- langchain
- langgraph
- langchain-openai
- langchain-community
- langchain-experimental

You can install the required packages using pip:
```bash
pip install langchain langgraph langchain-openai langchain-community langchain-experimental
