# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# # from langchain.agents import initialize_agent, Tool
# # from langchain.agents.agent_types import AgentType
# from langchain.agents import  AgentExecutor
# from Tools import search_web_tool

# load_dotenv()

# # Set up Groq LLM using LangChain
# llm = ChatGroq(
#     groq_api_key=os.getenv("GROQ_API_KEY"),
#     model_name="llama-3.1-8b-instant",     # or llama3-70b-8192
#     temperature=0.7
# )


# # Initialize LangChain agents using tools
# # guide_expert = initialize_agent(
# guide_expert = AgentExecutor(
#     tools=[search_web_tool],
#     llm=llm,
#     agent=AgentType.create_react_agent,
#     verbose=True,
#     agent_kwargs={
#         "prefix": "You are a local city guide helping users with places to visit.",
#     }
# )

# # location_expert = initialize_agent(
# location_expert = AgentExecutor(
#     tools=[search_web_tool],
#     llm=llm,
#     agent=AgentType.create_react_agent,
#     verbose=True,
#     agent_kwargs={
#         "prefix": "You are a travel logistics expert helping users with essential travel info.",
#     }
# )

# # planner_expert = initialize_agent(
# planner_expert = AgentExecutor(
#     tools=[search_web_tool],
#     llm=llm,
#     agent=AgentType.create_react_agent,
#     verbose=True,
#     agent_kwargs={
#         "prefix": "You are a professional travel planner. Use the information to build a travel plan.",
#     }
# )


import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from Tools import search_web_tool

# Load environment variables
load_dotenv()

# Initialize Groq LLM
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0.7
)

# ------------------------------
# 1. GUIDE EXPERT AGENT
# ------------------------------
guide_expert = initialize_agent(
    tools=[search_web_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "prefix": (
            "You are a friendly local city guide. "
            "Your job is to recommend attractions, food, activities, and local experiences. "
            "Always explain in simple terms and keep suggestions practical."
        )
    }
)

# ------------------------------
# 2. LOGISTICS / LOCATION EXPERT
# ------------------------------
location_expert = initialize_agent(
    tools=[search_web_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "prefix": (
            "You are a travel logistics expert. "
            "You help users with weather, transport, routes, timings, tickets, and safety information."
        )
    }
)

# ------------------------------
# 3. MAIN TRIP PLANNER EXPERT
# ------------------------------
planner_expert = initialize_agent(
    tools=[search_web_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs={
        "prefix": (
            "You are a professional travel planner. "
            "Combine all available information and create a complete itinerary. "
            "Your plans should be structured day-wise and easy to follow."
        )
    }
)

# # Export agents so app.py can import them
# __all__ = ["llm", "guide_expert", "location_expert", "planner_expert"]
