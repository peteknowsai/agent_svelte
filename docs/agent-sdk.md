# OpenAI Agents SDK (Python)

## 1. Installation
```bash
pip install openai-agents
```

## 2. Hello World
```python
from agents import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant"
)

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
print(result.final_output)
```

## 3. Function Tools
Any Python function becomes a tool with `@function_tool`.

```python
from typing_extensions import TypedDict
from agents import Agent, Runner, function_tool

class Location(TypedDict):
    lat: float
    long: float

@function_tool
async def fetch_weather(location: Location) -> str:
    """Fetch the weather for a given location."""
    return "sunny"

agent = Agent(
    name="WeatherAgent",
    tools=[fetch_weather]
)

result = Runner.run_sync(agent, "What's the weather in Paris?")
print(result.final_output)
```

## 4. Multi-Agent Workflows & Handoffs
```python
from agents import Agent, Runner

history = Agent(
    name="History Tutor",
    instructions="Assist with history questions",
    handoff_description="Specialist agent for history"
)
math = Agent(
    name="Math Tutor",
    instructions="Help with math problems",
    handoff_description="Specialist agent for math"
)
triage = Agent(
    name="Triage Agent",
    instructions="Route homework questions to the right specialist",
    handoffs=[history, math]
)

result = Runner.run_sync(triage, "What is the capital of France?")
print(result.final_output)
```

## 5. Guardrails
```python
from pydantic import BaseModel
from agents import Agent, Runner, GuardrailFunctionOutput

class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail Check",
    instructions="Detect if the user is asking homework questions",
    output_type=HomeworkOutput,
)

async def homework_guardrail(ctx, agent, input_data):
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )
```

## 6. FastAPI Streaming Integration

```python
# agents_app.py
import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent

app = FastAPI()

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant"
)

@app.post("/api/agent/stream")
async def stream_agent(request: Request):
    payload = await request.json()
    user_input = payload["input"]
    result = Runner.run_streamed(agent, input=user_input)

    async def event_generator():
        async for event in result.stream_events():
            # Only stream text delta events
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                chunk = event.data.delta
                yield f"data: {chunk}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
```

## 7. SvelteKit Vercel AI SDK

### 7.1 Installation

```bash
npm install ai @ai-sdk/openai @ai-sdk/svelte
```

### 7.2 SvelteKit Setup

Generate a new SvelteKit v5 project and install dependencies:
```bash
npm create svelte@latest my-sveltebot -- --template skeleton
cd my-sveltebot
npm install
```

### 7.3 API Route (`src/routes/api/chat/+server.ts`)

```ts
import { createOpenAI } from "@ai-sdk/openai";
import type { RequestHandler } from "./$types";

export const POST: RequestHandler = async ({ request }) => {
  const { messages } = await request.json();
  const openai = createOpenAI({ apiKey: process.env.OPENAI_API_KEY });
  const response = await openai.chat.completions.create({
    model: "gpt-4o",
    messages,
    stream: true
  });
  return new Response(response.body, {
    headers: { "Content-Type": "text/event-stream" }
  });
};
```

### 7.4 Chat Component (`src/routes/+page.svelte`)

```svelte
<script lang="ts">
  import { Chat } from "@ai-sdk/svelte";
  import { createOpenAI } from "@ai-sdk/openai";

  const chat = new Chat({
    api: {
      provider: createOpenAI({ apiKey: import.meta.env.VITE_OPENAI_API_KEY }),
      path: "/api/chat"
    }
  });
</script>

<main class="p-4">
  <div class="space-y-4">
    {#each $chat.messages as msg}
      <div class="{msg.role === 'user' ? 'text-right' : 'text-left'}">
        <div class="inline-block bg-gray-200 p-2 rounded">{msg.content}</div>
      </div>
    {/each}
  </div>

  <form on:submit|preventDefault={() => chat.submit()} class="mt-4 flex">
    <input
      bind:value={$chat.input}
      placeholder="Type your message..."
      class="flex-1 p-2 border rounded-l"
    />
    <button type="submit" class="px-4 bg-blue-600 text-white rounded-r">
      Send
    </button>
  </form>
</main>
```

### 7.5 Environment Variables

Create a `.env` file at project root:
```
VITE_OPENAI_API_KEY=your_openai_key
```

### 7.6 Summary

This section demonstrates how to integrate the Vercel AI SDK into a SvelteKit v5 app, creating a streaming chat UI with a server endpoint and a reactive Svelte component.
