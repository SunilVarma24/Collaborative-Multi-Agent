# main.py
from IPython.display import Image, display, Markdown
from src.graph import get_agent_graph, get_compiled_agent

def main():
    # Display the agent workflow graph
    agent_graph = get_agent_graph()
    display(Image(agent_graph.draw_mermaid_png()))
    
    # Test the multi-agent system with a sample prompt
    prompt = """Fetch the data of the top 10 car companies with the highest sales in the world.
    Then use this data and draw a bar chart."""
    
    response = get_compiled_agent().invoke({"messages": [("human", prompt)]}, {"recursion_limit": 150})
    display(Markdown(response['messages'][-1].content))

if __name__ == "__main__":
    main()
