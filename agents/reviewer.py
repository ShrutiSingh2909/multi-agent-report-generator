from crewai import Agent

def get_reviewer(llm):
    return Agent(
        role="Quality Reviewer",
        goal="Review and improve the report for accuracy, clarity, completeness and quality.",
        backstory="""You are a meticulous quality reviewer with high standards. 
        You ensure reports are accurate, complete, well-structured and 
        easy to understand. You improve clarity and fix any gaps.""",
        llm=llm,
        verbose=True,
        max_iter=3
    )