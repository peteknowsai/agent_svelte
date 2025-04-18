# Task List

## 1. Agent Backend (Python)
- [x] Create Python virtual environment
- [x] Install `openai-agents` SDK
- [x] Define a basic text-only agent in `agents-python/`
- [x] Write a test script (CLI) to call the agent locally using `Runner.run_sync`
- [x] Expose FastAPI endpoint at `/api/agent/stream` with POST
- [x] Implement streaming response from agent over HTTP using `Runner.run_streamed`
- [x] Document Python agent and FastAPI streaming in `docs/agent-sdk.md` and `docs/streaming-integration.md`

## 2. SvelteKit Chat UI
- [] Scaffold SvelteKit v5 project in `sveltekit/`
- [ ] Install Tailwind CSS + DaisyUI
- [] Install Vercel AI SDK (`ai`, `@ai-sdk/openai`, `@ai-sdk/svelte`)
- [] Build a basic streaming chat interface using `Chat` from `@ai-sdk/svelte`
- [] Enable streaming through `stream: true` in the chat config
- [] Style chat bubbles, loading, and error states
- [] Document SvelteKit setup in `docs/sveltekit-ai-sdk.md`

## 3. Integration
- [] Add custom Python agent provider pointing to `/api/agent/stream`
- [] Wire up UI to stream from backend agent endpoint
- [] Test end-to-end streaming chat flow
- [] Implement retry and error handling in UI
- [] Document the full pipeline in `docs/streaming-integration.md`

## 4. Documentation & Cleanup
- [] Update README with setup instructions for both backend and frontend
- [] Clean up lint and formatting errors in all docs
- [] Add CI scripts for backend tests and frontend linting
