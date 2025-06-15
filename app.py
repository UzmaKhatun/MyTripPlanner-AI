import os
import streamlit as st

# Import LLM and agents
from Agents import llm, guide_expert, location_expert, planner_expert
from Tasks import location_task, guide_task, planner_task

# Streamlit App Title
st.set_page_config(page_title="AI Travel Planner", page_icon="🌍", layout="wide")

# Main title and description
st.title("🌍 AI-Powered Trip Planner")

st.markdown("""
💡 **Plan your next trip with AI!**  
Enter your travel details below, and our AI-powered travel assistant will create a personalized itinerary including:
- Best places to visit  
- Local food recommendations  
- Transportation & visa tips  
- Budget & accommodation planning  
""")

# Create 2 columns
col1, col2 = st.columns(2)

with col1:
    from_city = st.text_input("🏡 From City", "India")
    date_from = st.date_input("📅 Departure Date")

with col2:
    destination_city = st.text_input("✈️ Destination City", "Rome")
    date_to = st.date_input("📅 Return Date")

interests = st.text_area("🎯 Your Interests (e.g., sightseeing, food, adventure)", "sightseeing and good food")

# Button to run planner
if st.button("🚀 Generate Travel Plan"):
    if not from_city or not destination_city or not date_from or not date_to or not interests:
        st.error("⚠️ Please fill in all fields before generating your travel plan.")
    else:
        st.info("⏳ AI is preparing your personalized travel itinerary... Please wait.")

        # Run tasks directly with LLM (not agent.llm)
        location_result = location_task(llm, from_city, destination_city, date_from, date_to)
        guide_result = guide_task(llm, destination_city, interests, date_from, date_to)
        final_plan = planner_task(
            llm=llm,
            context=f"{location_result}\n\n{guide_result}",
            destination_city=destination_city,
            interests=interests,
            date_from=date_from,
            date_to=date_to
        )

        # Display Results
        st.subheader("✅ Your AI-Powered Travel Plan")
        st.markdown(final_plan)

        # Download Button
        st.download_button(
            label="📥 Download Travel Plan (.md)",
            data=final_plan,
            file_name=f"Travel_Plan_{destination_city}.md",
            mime="text/markdown"
        )

