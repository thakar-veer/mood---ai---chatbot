# 🎭 Mood AI Chatbot

A Streamlit chatbot that lets you pick the AI's personality — **Sad**, **Happy**, or **Angry** — and responds to every message in that mood. Built with LangChain and Mistral AI.

## Features

- 🎭 Switch between three AI moods from the sidebar (Sad / Happy / Angry)
- 💬 Real-time chat interface with message history
- 🎨 UI theme (colors, avatars) changes dynamically based on the selected mood
- 🔄 "New Chat" button to reset the conversation at any time
- 🔒 API key kept out of source control via `.env`

## Tech Stack

- **Streamlit** – web UI
- **LangChain** – conversation/message orchestration
- **Mistral AI** (`mistral-small-2506`) – language model
- **python-dotenv** – environment variable management

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/mood-ai-chatbot.git
   cd mood-ai-chatbot
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API key**
   - Rename `.env.example` to `.env`
   - Add your Mistral AI API key:
     ```
     MISTRAL_API_KEY=your_mistral_api_key_here
     ```

5. **Run the app**
   ```bash
   streamlit run mood_ai_chatbot.py
   ```

   The app will open at `http://localhost:8501`.

## Project Structure

```
mood-ai-chatbot/
├── mood_ai_chatbot.py   # Main Streamlit app
├── requirements.txt     # Python dependencies
├── .env.example          # Template for environment variables
├── .gitignore
└── README.md
```

## How It Works

Each mood corresponds to a different `SystemMessage` sent to the LLM, which steers its tone for the entire conversation. Switching moods resets the chat so the personalities don't mix mid-conversation.

## License

This project is open source and available under the [MIT License](LICENSE).
