import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(page_title="Mood AI", page_icon="🎭", layout="centered")

MODES = {
    "😢 Sad": {
        "system": "You are a sad AI agent. Reply to every message in a sad, melancholic way.",
        "avatar": "😢",
        "accent": "#4A6FA5",
        "bg": "#eef2f7",
    },
    "😄 Happy": {
        "system": "You are a happy AI agent. Reply to every message in a cheerful, upbeat way.",
        "avatar": "😄",
        "accent": "#F2A93B",
        "bg": "#fff8ec",
    },
    "😠 Angry": {
        "system": "You are an angry AI agent. Reply to every message in an irritated, angry way.",
        "avatar": "😠",
        "accent": "#D64545",
        "bg": "#fdeeee",
    },
}


@st.cache_resource
def get_model():
    return ChatMistralAI(model="mistral-small-2506", temperature=0.9, max_tokens=200)


model = get_model()

# ---------------- Sidebar: mood selector ----------------
st.sidebar.title("🎭 Choose AI Mood")
selected_mode = st.sidebar.radio(
    "Pick a personality:", list(MODES.keys()), label_visibility="collapsed"
)

if "current_mode" not in st.session_state:
    st.session_state.current_mode = selected_mode
    st.session_state.messages = [SystemMessage(content=MODES[selected_mode]["system"])]

# Switching mood resets the conversation so the new personality starts fresh
if selected_mode != st.session_state.current_mode:
    st.session_state.current_mode = selected_mode
    st.session_state.messages = [SystemMessage(content=MODES[selected_mode]["system"])]

if st.sidebar.button("🔄 New Chat"):
    st.session_state.messages = [
        SystemMessage(content=MODES[st.session_state.current_mode]["system"])
    ]

mode_info = MODES[st.session_state.current_mode]

# ---------------- Mood-based styling ----------------
st.markdown(
    f"""
    <style>
        .main {{
            background-color: {mode_info['bg']};
        }}
        /* Force dark, readable text anywhere inside the light-colored main area */
        .main [data-testid="stMarkdownContainer"],
        .main [data-testid="stMarkdownContainer"] p,
        .main [data-testid="stMarkdownContainer"] span {{
            color: #2b2b2b !important;
        }}
        .main [data-testid="stMarkdownContainer"] h1 {{
            color: {mode_info['accent']} !important;
        }}
        [data-testid="stChatMessage"] {{
            border-radius: 14px;
        }}
        [data-testid="stChatInput"] textarea {{
            color: #2b2b2b !important;
        }}
        .stButton>button {{
            background-color: {mode_info['accent']};
            color: white !important;
            border-radius: 8px;
            border: none;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(f"{mode_info['avatar']} Mood AI Chatbot")
st.caption(f"Currently feeling: **{st.session_state.current_mode}**")

# ---------------- Chat history ----------------
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar=mode_info["avatar"]):
            st.write(message.content)

# ---------------- Chat input ----------------
prompt = st.chat_input("Type your message here...")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant", avatar=mode_info["avatar"]):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
        st.write(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))
