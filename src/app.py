import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

from modules.brochure.ui import brochure_tab
from modules.airline_assistant.ui import airline_tab
from modules.meeting_minutes.ui import meeting_minutes_tab

# ───── Setup ─────────────────────────────────────────────────────────────
load_dotenv()
openai = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL  = "gpt-4o-mini"

st.set_page_config(page_title="LLMPedia", layout="wide")
st.title("LLMPedia")

# ───── Tabs ──────────────────────────────────────────────────────────────
tabs = st.tabs([
    "📄 Brochure Builder",
    "✈️ Airline AI Assistant",
    "📝 Meeting Minutes"
])

with tabs[0]:
    brochure_tab(openai, MODEL)

with tabs[1]:
   airline_tab(openai, MODEL)

with tabs[2]:
   meeting_minutes_tab(openai, MODEL)