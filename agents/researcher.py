from crewai import Agent
from tools.search_tool import search_web
from tools.memory_tool import save_to_memory
from crewai.tools import tool

@tool("Search Web Tool")
def search_tool(query: str) -> str:
    """Search the web for information on a given query."""
    return search_web(query)

@tool("Save Memory Tool")
def save_memory_tool(content: str) -> str:
    """Save research findings to memory."""
    return save_to_memory("research", content, "research_1")

def get_researcher(llm):
    return Agent(
        role="Senior Research Analyst",
        goal="Research and collect comprehensive, accurate information about the given topic from the web.",
        backstory="""You are an expert research analyst with years of experience 
        in gathering and synthesizing information from multiple sources. 
        You are thorough, accurate and always verify information.""",
        tools=[search_tool, save_memory_tool],
        llm=llm,
        verbose=True,
        max_iter=5,
        max_rpm=3
    )