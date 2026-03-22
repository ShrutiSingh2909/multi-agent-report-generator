from crewai import Agent
from tools.memory_tool import retrieve_from_memory
from crewai.tools import tool

@tool("Retrieve Memory Tool")
def retrieve_memory_tool(query: str) -> str:
    """Retrieve relevant research from memory."""
    return retrieve_from_memory(query)

def get_analyst(llm):
    return Agent(
        role="Data Analyst",
        goal="Analyze the research findings and extract key insights, patterns and important points.",
        backstory="""You are a skilled data analyst who excels at finding 
        patterns and insights in complex information. You break down 
        information into clear, actionable insights.""",
        tools=[retrieve_memory_tool],
        llm=llm,
        verbose=True,
        max_iter=2,
        max_rpm=2
    )