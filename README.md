# Small AI Chatbot

Minimal chatbot project built with FastAPI and the OpenAI Python SDK.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
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

## Python Version Note

If dependency installation fails on a very new Python release such as `Python 3.14`, recreate the virtual environment with `Python 3.12` or `Python 3.13`. Some packages may lag behind new interpreter releases with prebuilt wheels.

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
