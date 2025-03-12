# 🚀 Ollama AI API Client

A powerful Python client to interact with the **Ollama AI API**, allowing you to generate AI-powered text responses efficiently.

## 📌 Features
- 🔥 **Streaming Response** for real-time AI interaction.
- ⚙️ **Environment Configuration** using `.env` file.
- 🚀 **Error Handling** to manage API failures gracefully.
- 🏎️ **Optimized Performance** with efficient request handling.

---

## 📦 Installation

1️⃣ **Clone the Repository:**
```sh
git clone https://github.com/yourusername/OllamaAi.git
cd OllamaAi
```

2️⃣ **Create a Virtual Environment (Optional but Recommended):**
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3️⃣ **Install Dependencies:**
```sh
pip install -r requirements.txt
```

4️⃣ **Set Up Environment Variables:**
Create a `.env` file in the project directory and add:
```ini
OLLAMA_URL=http://localhost:11434/api/generate
OLLAMA_MODEL=phi4-mini
```

---

## 🚀 Usage

Run the script and enter your prompt:
```sh
python app.py
```

Example interaction:
```
Enter your prompt: Tell me a joke
💡 Generated Output:
Why did the AI cross the road? To optimize the other side! 😂
```

---

## 🛠 Requirements
- Python 3.8+
- `requests`
- `python-dotenv`

Install missing dependencies:
```sh
pip install requests python-dotenv
```

---

## 🤝 Contributing
Pull requests are welcome! Feel free to open an issue if you find a bug or have a feature request.

---

## 📜 License
MIT License. See `LICENSE` for details.

---

## ⭐ Support the Project
If you like this project, consider giving it a ⭐ on GitHub!

---

Happy Coding! 🚀

