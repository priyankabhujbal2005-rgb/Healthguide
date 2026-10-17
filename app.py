
import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="HealthGuide | AI Health Assistant",
    page_icon="🩺",
    layout="centered"
)

st.markdown("""

<style>
/* Main page background and default text */
.stApp {
    background: linear-gradient(135deg, #eef7ff, #f5f3ff);
    color: #1e293b;
}

.stApp, .stApp p, .stApp label,
.stApp span, .stApp li {
    color: #1e293b;
}

/* Main heading */
.main-title {
    text-align: center;
    color: #155e75 !important;
    font-size: 40px;
    font-weight: 800;
}

.subtitle {
    text-align: center;
    color: #334155 !important;
    font-size: 16px;
}

/* Chat messages */
div[data-testid="stChatMessage"] {
    background-color: #ffffff;
    border: 1px solid #cbd5e1;
    border-radius: 14px;
    padding: 12px;
}

div[data-testid="stChatMessage"] p,
div[data-testid="stChatMessage"] li,
div[data-testid="stChatMessage"] span {
    color: #1e293b !important;
}

/* Chat input */
.stChatInput textarea {
    color: #1e293b !important;
    background-color: #ffffff !important;
}

.stChatInput textarea::placeholder {
    color: #64748b !important;
}

/* Buttons */
div.stButton > button {
    background-color: #ffffff;
    color: #155e75 !important;
    border: 1px solid #94a3b8;
    border-radius: 10px;
}

div.stButton > button:hover {
    background-color: #dbeafe;
    border-color: #0284c7;
}

/* Expanders and general text */
div[data-testid="stExpander"] {
    background-color: #ffffff;
    border-radius: 10px;
}

[data-testid="stAlert"] p {
    color: #1e293b !important;
}

/* Links */
.stApp a {
    color: #0369a1 !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title">🩺 HealthGuide</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Your AI-powered health information assistant</div>',
    unsafe_allow_html=True
)

st.write(" ")
st.info(
    "HealthGuide provides general educational information, "
    "not medical diagnoses or prescriptions."
)

with st.expander("⚠️ Important health and safety information"):
    st.write(
        "If you may be experiencing a medical emergency, "
        "contact local emergency services immediately. "
        "Do not delay care while using this application. "
        "Automated keyword checks may miss emergencies."
    )

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "Hello! 👋 I'm HealthGuide. Ask me a general "
                "health question to get started."
            ),
            "source": "",
            "status": "welcome"
        }
    ]

from symptom_checker import show_symptom_checker

symptom_tab = st.tabs(["🩺 Symptom Checker"])[0]

with symptom_tab:
    show_symptom_checker()

# Display the conversation
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message.get("status") == "urgent":
            st.error("Potential emergency: seek immediate help.")

	
       
        if message.get("source"):
            st.markdown(
                f"**Trusted health reference:** "
                f"[Open original source]({message['source']})"
            )


        
	# Suggested questions
st.markdown("### 💡 Try asking")
suggestions = [
    "What causes a headache?",
    "How can I stay hydrated?",
    "What is a balanced diet?",
    "How can I improve my sleep?"
]

cols = st.columns(2)
for index, question in enumerate(suggestions):
    with cols[index % 2]:
        if st.button(question, key=f"suggestion_{index}"):
            st.session_state.pending_question = question

# Chat input
user_question = st.chat_input("Type your health question here...")

if user_question:
    st.session_state.pending_question = user_question

if st.session_state.get("pending_question"):
    question = st.session_state.pop("pending_question")

    st.session_state.messages.append({
        "role": "user",
        "content": question,
        "source": "",
        "status": "user"
    })

    response = get_response(question)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response["answer"],
        "source": response["source"],
        "status": response["status"]
    })

    st.rerun()
