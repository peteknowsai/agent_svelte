import os
import asyncio
import argparse
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

app = FastAPI()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant"
)

@app.post("/api/agent/stream")
async def stream_agent(request: Request):
    payload = await request.json()
    # support both `input` (string) or `messages` (array) payloads
    user_input = payload.get("input") or payload.get("messages")
    result = Runner.run_streamed(agent, input=user_input)

    async def event_generator():
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                chunk = event.data.delta
                yield f"data: {chunk}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )


def main():
    parser = argparse.ArgumentParser(description="Run the text-only agent CLI")
    parser.add_argument("input", nargs="?", default="Hello!", help="Prompt for the agent")
    args = parser.parse_args()
    result = Runner.run_sync(agent, args.input)
    print(result.final_output)


if __name__ == "__main__":
    main()
