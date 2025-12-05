import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

URL = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    # Required by OpenRouter (identify your app)
    "HTTP-Referer": "http://localhost",
    "X-Title": "Python Console Chat"
}

messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("OpenRouter Console Chat (type 'quit' to exit)")
print("-" * 50)

while True:
    user_input = input("You: ")

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    body = {
        "model": "meta-llama/llama-3.1-70b-instruct",
        "messages": messages
    }

    response = requests.post(URL, headers=headers, json=body)
    data = response.json()

    # ---------- ERROR HANDLING ----------
    if "error" in data:
        print("\n❌ API Error:")
        print(data["error"])
        print()
        continue  # don't crash
    # ------------------------------------

    # Parse assistant response safely
    try:
        ai_message = data["choices"][0]["message"]["content"]
    except KeyError:
        print("\n❌ Unexpected response format:")
        print(data)
        print()
        continue

    print(f"AI: {ai_message}")

    messages.append({"role": "assistant", "content": ai_message})