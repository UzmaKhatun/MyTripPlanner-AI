from langchain_community.tools import DuckDuckGoSearchResults
from langchain.agents import Tool

# Function to run search
def search_web(query: str) -> str:
    """
    Searches the web and returns results.
    """
    search_tool = DuckDuckGoSearchResults(num_results=10, verbose=True)
    return search_tool.run(query)

# LangChain-compatible Tool object
search_web_tool = Tool(
    name="Web Search Tool",
    func=search_web,
    description="Useful for answering travel-related questions by searching the web."
)
