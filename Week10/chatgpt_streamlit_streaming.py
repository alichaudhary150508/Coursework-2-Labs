import streamlit as st
import openai

# Initialize OpenAI client (NEW API)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Page configuration
st.set_page_config(
    page_title="GPT Assistant",
    page_icon="🧠",
    layout="wide"
)

# Title
st.title("🧠 ChatGPT – Streamlit + OpenAI API")
st.caption("Powered by GPT-4")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.header("🧰 Chat Controls")

    st.metric("Messages in chat", len(st.session_state.messages))

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    model = st.selectbox(
        "Model",
        ["gpt-4", "gpt-4.1"],  # Adjust as per available models
        index=0
    )

    temperature = st.slider(
        "Temperature",
        0.0, 2.0, 1.0, 0.1,
        help="Higher values make output more random"
    )

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Say something...")

if prompt:

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Save user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    # Assistant response (STREAMING)
    with st.chat_message("assistant"):

        # Use the new ChatCompletion API
        stream = openai.ChatCompletion.create(
            model=model,
            messages=st.session_state.messages,
            temperature=temperature,
            stream=True
        )

        container = st.empty()
        full_reply = ""

        # Process the stream and show the response
        for chunk in stream:
            if 'choices' in chunk and 'delta' in chunk['choices'][0] and 'content' in chunk['choices'][0]['delta']:
                full_reply += chunk['choices'][0]['delta']['content']
                container.markdown(full_reply + "▌")

        container.markdown(full_reply)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": full_reply}
    )