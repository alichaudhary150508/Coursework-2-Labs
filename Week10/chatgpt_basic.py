import requests

API_KEY = "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"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "HTTP-Referer": "http://localhost:8502/",  # or your project URL
    "X-Title": "My Python Coursework App"
}

data = {
    "model": "meta-llama/llama-3.1-8b-instruct:free",  # free model example
    "messages": [
        {"role": "user", "content": "Hello! Write me a Python function."}
    ]
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=data
)

print(response.json())