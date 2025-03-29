# src/tools.py
from typing import Annotated
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from langchain_experimental.utilities import PythonREPL

# Initialize tools
tv_search = TavilySearchResults(max_results=5, search_depth='advanced', max_tokens=10000)
repl = PythonREPL()

@tool
def python_repl(code: Annotated[str, "The python code to generate the chart."]) -> str:
    """Use this to execute python code.
       If you want to see the output of a value,
       you should print it out with `print(...)`.
       This is visible to the user.
    """
    try:
        result = repl.run(code)
    except BaseException as e:
        return f"Failed to execute. Error: {repr(e)}"
    result_str = f"Successfully executed:\n```python\n{code}\n```\nStdout: {result}"
    return result_str + "\n\nIf you have completed all tasks, respond with FINAL ANSWER."
