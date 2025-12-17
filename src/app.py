import os
from dotenv import load_dotenv
import streamlit as st
from google import genai

from modules.brochure.ui import brochure_tab
from modules.airline_assistant.ui import airline_tab
from modules.meeting_minutes.ui import meeting_minutes_tab
from modules.vision_chef.ui import vision_chef_tab
from modules.code_architect.ui import code_architect_tab

# ───── Setup ─────────────────────────────────────────────────────────────
st.set_page_config(page_title="LLMPedia", layout="wide")

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY not found in .env")
    st.stop()

client = genai.Client(api_key=api_key)
MODEL = "gemini-flash-latest"

st.title("LLMPedia")

# ───── Tabs ──────────────────────────────────────────────────────────────
tabs = st.tabs([
    "🏗️ Code Architect",
    "�‍🍳 Vision Chef",
    "�📄 Brochure Builder",
    "✈️ Airline AI Assistant",
    "📝 Meeting Minutes"
])

with tabs[0]:
    code_architect_tab(client, MODEL)

with tabs[1]:
    vision_chef_tab(client, MODEL)

with tabs[2]:
    brochure_tab(client, MODEL)

with tabs[3]:
   airline_tab(client, MODEL)

with tabs[4]:
   meeting_minutes_tab(client, MODEL)