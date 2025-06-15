# 🧳 AI Travel Planner

An AI-powered travel assistant built with **LangChain**, **Groq**, and **Streamlit**. It helps users generate detailed travel plans by gathering local guides, destination information, and itinerary suggestions with the help of intelligent agents.

---

## ✨ Features

- 🌍 Destination recommendations based on user interests  
- 📅 Generates personalized daily itineraries  
- 💬 Multi-agent system for guide, location info, and planner tasks  
- 📥 Downloadable markdown travel plan  
- ⚡ Powered by LLaMA 3 via Groq API  

---

## 🚀 How It Works

The app uses 3 AI agents:
- **Guide Expert** – Suggests attractions, food, and events  
- **Location Expert** – Gives visa info, accommodations, and logistics  
- **Planner Expert** – Compiles everything into a structured travel plan  

Each agent uses its own tools, allowing smart collaboration to generate a complete itinerary.

---

## 🛠️ Tech Stack

- `Python`
- `LangChain`
- `Groq API`
- `Streamlit`
- `Markdown for output formatting`

---

## 📂 Project Structure

Travel Agent/
- ├── app.py # Streamlit frontend
- ├── Agents.py # Agent initialization logic
- ├── Tasks.py # Prompt logic for each agent task
- ├── Tools.py # External tools (e.g., web search)
- ├── requirements.txt # Python dependencies
- ├── .env # API keys
- ├── Travel_Plan_Kashmir.md # Sample output
- └── .gitignore # Ignores venv and secrets

---

## Create virtual environment & activate it
```
python -m venv venv
venv\Scripts\activate   # On Windows
```

## Install dependencies
```
pip install -r requirements.txt
```

## Add your .env file
```
GROQ_API_KEY=your_groq_api_key_here
```

## Run the app
```
streamlit run app.py
```

## 📄 Example Output

- Travel plans are generated in [Travel_Plane_Kashmir.md](https://github.com/UzmaKhatun/MyTripPlanner-AI/blob/main/Travel_Plan_Kashmir.md) format
- Downloadable directly from the app

---

## 🙌 Credits
Created with ❤️ using LangChain and Groq's blazing-fast LLaMA 3 models.

---

## Author
Uzma Khatun<br>
🔗 Connect on [LinkedIn](
https://www.linkedin.com/in/uzma-khatun-88b990334/
)
