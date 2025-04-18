# SvelteKit Vercel AI SDK

This guide covers setting up a streaming chat UI in SvelteKit v5 using the Vercel AI SDK.

## 1. Installation

```bash
npm install ai @ai-sdk/openai @ai-sdk/svelte
```

## 2. SvelteKit Project Setup

Scaffold a SvelteKit v5 app and install dependencies:

```bash
npm create svelte@latest my-sveltebot -- --template skeleton
cd my-sveltebot
npm install
```

## 3. API Route (`src/routes/api/chat/+server.ts`)

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

## 4. Chat Component (`src/routes/+page.svelte`)

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

## 5. Environment Variables

Create a `.env` at project root:

```
VITE_OPENAI_API_KEY=your_openai_key
```

---
*For detailed Python backend streaming and FastAPI integration, see [agent-sdk.md](./agent-sdk.md).*
