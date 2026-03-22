from crewai import Crew, Task, LLM
from agents.researcher import get_researcher
from agents.analyst import get_analyst
from agents.writer import get_writer
from agents.reviewer import get_reviewer
import os
import time
from dotenv import load_dotenv

load_dotenv()

def build_crew(topic: str):
    """Build and run the multi-agent crew for the given topic."""

    # Initialize Gemini LLM
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        api_key=os.getenv("GROQ_API_KEY"),
        max_tokens=1024,
        temperature=0.3
    )

    # Initialize agents
    researcher = get_researcher(llm)
    analyst    = get_analyst(llm)
    writer     = get_writer(llm)
    reviewer   = get_reviewer(llm)

    # Define tasks
    research_task = Task(
        description=f"""Research the topic: '{topic}'
        Search the web for comprehensive and recent information.
        Collect at least 5 key points and save findings to memory.
        Focus on facts, statistics and recent developments.""",
        expected_output="Detailed research findings with key facts, statistics and sources.",
        agent=researcher
    )

    analysis_task = Task(
        description=f"""Analyze the research findings about '{topic}'.
        Retrieve information from memory and identify:
        - Key trends and patterns
        - Important statistics
        - Main challenges and opportunities
        - Future outlook""",
        expected_output="Structured analysis with key insights, trends and patterns.",
        agent=analyst
    )

    writing_task = Task(
        description=f"""Write a comprehensive report about '{topic}' based on the analysis.
        Structure the report with:
        # {topic}
        ## Executive Summary
        ## Key Findings
        ## Detailed Analysis
        ## Trends and Patterns
        ## Challenges and Opportunities
        ## Future Outlook
        ## Conclusion
        Make it professional, clear and engaging.""",
        expected_output="Complete well-structured markdown report with all sections.",
        agent=writer
    )

    review_task = Task(
        description=f"""Review and improve the report about '{topic}'.
        Check for:
        - Accuracy and completeness
        - Clarity and readability
        - Proper structure and flow
        - Missing important points
        Return the final improved report.""",
        expected_output="Final polished report ready for download.",
        agent=reviewer
    )

    # Build crew
    crew = Crew(
        agents=[researcher, analyst, writer],
        tasks=[research_task, analysis_task, writing_task],
        verbose=True,
        step_callback=lambda x: time.sleep(10)
    )

    return crew