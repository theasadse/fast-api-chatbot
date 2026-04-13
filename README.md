# Small AI Chatbot

Minimal chatbot project built with FastAPI and the OpenAI Python SDK.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Set `OPENAI_API_KEY` in `.env` or export it in your shell.

## Run

```bash
source .venv/bin/activate
python app.py
```

Open `http://127.0.0.1:8000`.

## API

`POST /api/chat`

Request body:

```json
{
  "message": "Hello"
}
```

Response body:

```json
{
  "reply": "Hi! How can I help?"
}
```
