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
# Custom CSS for cleaner UI
# -------------------------------------------------------
st.markdown("""
<style>
/* Chat message styling */
.user-msg {
    background-color: #e8f0ff;
    padding: 12px 16px;
    border-radius: 10px;
    margin-bottom: 8px;
}

.bot-msg {
    background-color: #ecfcd7;
    padding: 12px 16px;
    border-radius: 10px;
    margin-bottom: 8px;
}

/* Remove Streamlit padding */
.block-container {
    padding-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

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
# Display Chat Messages
# -------------------------------------------------------
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-msg'>🧑‍💼 <b>You:</b><br>{msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-msg'>🤖 <b>Bot:</b><br>{msg['content']}</div>", unsafe_allow_html=True)

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

    st.markdown(f"<div class='user-msg'>🧑‍💼 <b>You:</b><br>{query}</div>", unsafe_allow_html=True)

    # Bot Processing
    with st.spinner("🔍 Searching the internet..."):
        result = search_chain.run(query)

    # Store bot response
    st.session_state.messages.append({"role": "assistant", "content": result})

    st.markdown(f"<div class='bot-msg'>🤖 <b>Bot:</b><br>{result}</div>", unsafe_allow_html=True)
