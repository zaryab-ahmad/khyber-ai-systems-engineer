import os
import json
import asyncio
from typing import AsyncIterable

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

# 2026 Unified Agent Architecture Imports
from langchain_mistralai import ChatMistralAI
from langchain.agents import create_agent

# 1. Initialize FastAPI App
app = FastAPI(
    title="Industrial AI Agent API",
    description="High-performance Mistral backend with streaming and Pydantic validation.",
    version="1.0.0"
)

# 2. Configure Environment & Model
# Replace with your actual key or ensure it is set in your environment
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY", "your-mistral-key-here")

llm = ChatMistralAI(
    model="mistral-large-latest", 
    temperature=0,
    streaming=True  # Enables token-by-token generation
)

# 3. Define the Agent Logic
# For Task 3, we define a standard agent. You can add tools=[] here if needed.
agent = create_agent(
    model=llm,
    tools=[], 
    system_prompt="You are a high-performance industrial AI assistant. Provide concise, technical responses."
)

# 4. Data Validation (Pydantic Schemas)
class ChatRequest(BaseModel):
    """Strict schema for incoming user queries."""
    message: str = Field(..., description="The user's question or command.", example="Explain the benefits of FastAPI.")

# 5. Streaming Generator Logic (SSE)
async def event_generator(user_message: str) -> AsyncIterable[str]:
    """
    Handles asynchronous inference and formats output as Server-Sent Events (SSE).
    Uses the 'messages' format required by the 2026 Mistral API.
    """
    input_payload = {
        "messages": [{"role": "user", "content": user_message}]
    }

    try:
        # .astream() handles the multi-step reasoning loop asynchronously
        async for event in agent.astream(input_payload, stream_mode="messages"):
            # In 2026 LangChain, we filter for actual message content updates
            if event and len(event) > 0:
                token = event[0].content
                if token:
                    # Format as standard SSE (data: <payload>\n\n)
                    yield f"data: {json.dumps({'token': token})}\n\n"
            
            # Small sleep to prevent CPU spiking in high-concurrency environments
            await asyncio.sleep(0.01)
            
    except Exception as e:
        yield f"data: {json.dumps({'error': str(e)})}\n\n"

# 6. API Endpoints
@app.get("/", tags=["Status"])
async def root():
    """Health check endpoint."""
    return {
        "status": "Online",
        "documentation": "/docs",
        "version": "2026.1"
    }

@app.post("/stream", tags=["AI Operations"])
async def stream_chat(request: ChatRequest):
    """
    Endpoint for real-time AI response streaming.
    Returns a Server-Sent Events (SSE) stream.
    """
    return StreamingResponse(
        event_generator(request.message), 
        media_type="text/event-stream"
    )

# 7. Local Runner Logic
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)