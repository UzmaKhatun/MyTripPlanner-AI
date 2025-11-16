import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from Tools import search_web_tool

load_dotenv()

# Set up Groq LLM using LangChain
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",     # or llama3-70b-8192
    temperature=0.7
)


# Initialize LangChain agents using tools
guide_expert = initialize_agent(
    tools=[search_web_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "prefix": "You are a local city guide helping users with places to visit.",
    }
)

location_expert = initialize_agent(
    tools=[search_web_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "prefix": "You are a travel logistics expert helping users with essential travel info.",
    }
)

planner_expert = initialize_agent(
    tools=[search_web_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "prefix": "You are a professional travel planner. Use the information to build a travel plan.",
    }
)
