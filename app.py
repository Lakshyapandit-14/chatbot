import streamlit as st
import os
from dotenv import load_dotenv

from core.tavily_tool import TavilySearch
from core.search_chain import SearchChain

# -------------------------------------------------------
# Load ENV variables
# -------------------------------------------------------
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

if not TAVILY_API_KEY:
    st.error("❌ Missing TAVILY_API_KEY in .env")
    st.stop()

# -------------------------------------------------------
# Dependency Injection
# -------------------------------------------------------
tavily_service = TavilySearch(api_key=TAVILY_API_KEY)
search_chain = SearchChain(service=tavily_service)

# -------------------------------------------------------
# Streamlit Page Config
# -------------------------------------------------------
st.set_page_config(
    page_title="lakshya Search Bot",
    page_icon="🔎",
    layout="wide"
)

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    st.info(
        "This bot uses **Tavily Search API** + **LangChain**.\n\n"
        "Ask anything and it will search the web in real time."
    )

# -------------------------------------------------------
# Main Title
# -------------------------------------------------------
st.title("🔎 lakshya Search Bot")
st.caption("Powered by Tavily + LangChain")

# -------------------------------------------------------
# Chat Initialization
# -------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------------------------------
# Display Chat Messages (using Streamlit chat UI)
# -------------------------------------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.write(msg["content"])
    else:
        with st.chat_message("assistant"):
            st.write(msg["content"])

# -------------------------------------------------------
# User Input
# -------------------------------------------------------
query = st.chat_input("Ask something...")

# -------------------------------------------------------
# On Submit
# -------------------------------------------------------
if query:
    # Store user message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.write(query)

    # Bot Processing
    with st.chat_message("assistant"):
        with st.spinner("🔍 Searching the internet..."):
            result = search_chain.run(query)
        st.write(result)

    # Store bot response
    st.session_state.messages.append({"role": "assistant", "content": result})
