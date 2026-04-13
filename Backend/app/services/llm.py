import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_ai_response(user_message: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": user_message,
                "stream": False
            }
        )

        data = response.json()
        return data.get("response", "No response from model")

    except Exception as e:
        print("Error:", e)
        return "Error connecting to Ollama"