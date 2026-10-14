from fastapi import APIRouter, HTTPException, Depends
from groq import Groq
from dotenv import load_dotenv
from ..config import settings
from .. import schemas, oauth2

# Load environment variables from .env file
load_dotenv()

router = APIRouter(prefix="/ai", tags=["AI Integration (Groq Cloud)"])

# Initialize the official Groq client
client = Groq(api_key=settings.groq_api_key)

# Use an active production model ID
MODEL_NAME = "openai/gpt-oss-20b"


@router.post("/chat", response_model=schemas.ChatResponse)
def chat_with_llm(
    payload: schemas.ChatRequest, current_user: int = Depends(oauth2.get_current_user)
):
    """
    Handles a basic conversational prompt via Groq's cloud API.
    """
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful, direct software engineering assistant.",
                },
                {"role": "user", "content": payload.prompt},
            ],
        )

        reply_text = completion.choices[0].message.content
        return {"reply": reply_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/summarize", response_model=schemas.SummaryResult)
def summarize_text(
    payload: schemas.SummarizeRequest,
    current_user: int = Depends(oauth2.get_current_user),
):
    """
    Calls Groq using standard JSON mode and validates with Pydantic.
    """
    try:
        completion = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "system",
                    "content": "Analyze the provided text and extract a structured summary. You must return a valid JSON object with keys: 'title' (string), 'key_points' (array of 3 strings), and 'sentiment' (string: positive, neutral, or negative).",
                },
                {"role": "user", "content": payload.text},
            ],
            response_format={"type": "json_object"},
        )
        raw_content = completion.choices[0].message.content

        # Parse and validate the raw JSON string using your Pydantic model
        parsed_output = schemas.SummaryResult.model_validate_json(raw_content)
        return parsed_output

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
