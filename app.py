import requests
import json
import time
import os
from dotenv import load_dotenv

# 🎯 Load environment variables
load_dotenv()
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
DEFAULT_MODEL = os.getenv("OLLAMA_MODEL", "phi4-mini")

def generate_text(prompt: str, model: str = DEFAULT_MODEL, stream: bool = True) -> str:
    """
    Sends a request to Ollama API and retrieves the response.
    
    :param prompt: User input text
    :param model: Model name (default: phi4-mini)
    :param stream: Enable/disable streaming response
    :return: Generated text from the model
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    try:
        start_time = time.time()
        response = requests.post(OLLAMA_URL, json=payload, stream=stream)
        response.raise_for_status()  # Raise error for HTTP failures

        if stream:
            print("🔄 Streaming response:\n")
            full_response = ""
            for chunk in response.iter_lines():
                if chunk:
                    data = json.loads(chunk.decode('utf-8'))
                    text = data.get("response", "")
                    print(text, end="", flush=True)
                    full_response += text
            return full_response
        
        return response.json().get("response", "")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: {e}")
        return "Error occurred while generating text."
    finally:
        elapsed_time = time.time() - start_time
        print(f"\n⏳ Time taken: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    user_input = input("Enter your prompt: ")
    output = generate_text(user_input)
    print("\n\n💡 Generated Output:\n", output)
