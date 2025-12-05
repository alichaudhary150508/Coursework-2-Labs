import streamlit as st
from openai import OpenAI

# Initialize OpenRouter client (IMPORTANT!)
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"],
    base_url="https://openrouter.ai/api/v1"
)

# Page title
st.title("Cybersecurity AI Assistant")

# Initialize session state with system prompt
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "system",
            "content": (
                "You are a cybersecurity expert assistant. "
                "Analyze threats, incidents, CVEs, MITRE ATT&CK mappings, "
                "and provide mitigation strategies in a technical, precise tone."
            )
        }
    ]

# Display history (excluding system)
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).markdown(msg["content"])

# User input box
prompt = st.chat_input("Ask about cybersecurity...")

if prompt:
    # Show user message
    st.chat_message("user").markdown(prompt)

    # Add to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Call OpenRouter API
    response = client.chat.completions.create(
        model="openai/gpt-4.1-mini",     # OpenRouter model name
        messages=st.session_state.messages
    )

    ai_message = response.choices[0].message.content

    # Display assistant message
    st.chat_message("assistant").markdown(ai_message)

    # Save assistant reply
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_message}
    )