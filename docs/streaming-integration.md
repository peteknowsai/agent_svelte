# Streaming Integration Guide

This document explains how to wire up streaming from the Python agent, through FastAPI, to a SvelteKit frontend.

## 1. Python Agent: Streaming Output

We use `Runner.run_streamed` to emit token‐level updates in real time.

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

## 2. FastAPI SSE Endpoint Details

- **URL**: `/api/agent/stream`
- **Response**: `text/event-stream` (SSE)
- **Protocol**: Each token is sent as a `data:` line, separated by double newline.

## 3. SvelteKit Frontend: Consuming the Stream

### 3.1 Low‑Level `EventSource` Example

```svelte
<script lang="ts">
  let input = ""
  let messages: { role: string; content: string }[] = []

  function send() {
    messages.push({ role: "user", content: input })
    let buffer = ""
    const es = new EventSource("/api/agent/stream")

    es.onmessage = (e) => {
      buffer += e.data
      const last = messages[messages.length - 1]
      if (last?.role === "assistant") {
        last.content = buffer
      } else {
        messages.push({ role: "assistant", content: buffer })
      }
    }

    es.onerror = () => es.close()
  }
</script>

<main>
  {#each messages as msg}
    <div class={msg.role}>{msg.content}</div>
  {/each}

  <form on:submit|preventDefault={send}>
    <input bind:value={input} placeholder="Type..." />
    <button type="submit">Send</button>
  </form>
</main>
```

### 3.2 Vercel AI SDK `Chat` Example

```svelte
<script lang="ts">
  import { Chat } from "@ai-sdk/svelte"
  import { createOpenAI } from "@ai-sdk/openai"

  const chat = new Chat({
    api: {
      provider: createOpenAI({ apiKey: import.meta.env.VITE_OPENAI_API_KEY }),
      path: "/api/agent/stream"
    }
  })
</script>

<template>
  <!-- same UI as before, bound to $chat.messages and $chat.input -->
</template>
```

## 4. Environment Variables

- **Python**:  `.env` → `OPENAI_API_KEY=your_key`
- **SvelteKit**: `.env` → `VITE_OPENAI_API_KEY=your_key`

## 5. Summary

End‑to‑end streaming from the agent via FastAPI SSE to SvelteKit ensures low‑latency, real‑time chat updates. Feel free to adapt this pipeline to other frameworks!
