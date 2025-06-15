from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# --- Location Info Task ---
def location_task(llm, from_city, destination_city, date_from, date_to):
    prompt = PromptTemplate.from_template("""
    In French: Provide travel-related information including accommodations, cost of living,
    visa requirements, transportation, weather, and local events.

    Traveling from: {from_city}
    Destination: {destination_city}
    Arrival Date: {date_from}
    Departure Date: {date_to}

    Respond in FRENCH if the destination is in a French-speaking country.
    """)
    return LLMChain(llm=llm, prompt=prompt).run(
        from_city=from_city,
        destination_city=destination_city,
        date_from=date_from,
        date_to=date_to
    )


# --- Local Guide Task ---
def guide_task(llm, destination_city, interests, date_from, date_to):
    prompt = PromptTemplate.from_template("""
    Provide a travel guide with attractions, food recommendations, and events.
    Tailor recommendations based on user interests: {interests}.
    
    Destination: {destination_city}
    Arrival Date: {date_from}
    Departure Date: {date_to}
    """)
    return LLMChain(llm=llm, prompt=prompt).run(
        destination_city=destination_city,
        interests=interests,
        date_from=date_from,
        date_to=date_to
    )


# --- Travel Plan Compilation Task ---
def planner_task(llm, context, destination_city, interests, date_from, date_to):
    prompt = PromptTemplate.from_template("""
    Based on the following context, combine all information into a well-structured itinerary. Include:
    - City introduction (4 paragraphs)
    - Daily travel plan with time allocations
    - Expenses and tips
    - Be in **Markdown format**
    - Include headings for each day
    - Summarize key events and places visited
    - Mention meals, local flavors, and unique cultural experiences
    - Add estimated expenses and tips at the end in a table if possible

    CONTEXT: {context}

    Destination: {destination_city}
    Interests: {interests}
    Arrival: {date_from}
    Departure: {date_to}
    """)
    return LLMChain(llm=llm, prompt=prompt).run(
        context=context,
        destination_city=destination_city,
        interests=interests,
        date_from=date_from,
        date_to=date_to
    )
