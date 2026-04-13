import os
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent
STATIC_DIR = BASE_DIR / "static"

load_dotenv()


app = FastAPI(title="Small AI Chatbot")
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)


class ChatResponse(BaseModel):
    reply: str


def get_client() -> OpenAI:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="OPENAI_API_KEY is not set. Add it to your environment before starting the app.",
        )
    return OpenAI(api_key=api_key)


@app.get("/", response_class=HTMLResponse)
def index() -> str:
    return (STATIC_DIR / "index.html").read_text(encoding="utf-8")


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    client = get_client()
    model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

    try:
        response = client.responses.create(
            model=model,
            input=[
                {
                    "role": "system",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "You are a concise and helpful assistant for a small demo chatbot.",
                        }
                    ],
                },
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": payload.message}],
                },
            ],
        )
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"OpenAI request failed: {exc}") from exc

    return ChatResponse(reply=response.output_text.strip())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
