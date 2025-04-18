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
- [x] Scaffold SvelteKit v5 project in `sveltekit/`
- [ ] Install Tailwind CSS + DaisyUI
- [x] Install Vercel AI SDK (`ai`, `@ai-sdk/openai`, `@ai-sdk/svelte`)
- [x] Build a basic streaming chat interface using `Chat` from `@ai-sdk/svelte`
- [x] Enable streaming through `stream: true` in the chat config
- [x] Style chat bubbles, loading, and error states
- [x] Document SvelteKit setup in `docs/sveltekit-ai-sdk.md`

## 3. Integration
- [x] Add custom Python agent provider pointing to `/api/agent/stream`
- [x] Wire up UI to stream from backend agent endpoint
- [x] Test end-to-end streaming chat flow
- [x] Implement retry and error handling in UI
- [x] Document the full pipeline in `docs/streaming-integration.md`

## 4. Documentation & Cleanup
- [ ] Update README with setup instructions for both backend and frontend
- [x] Clean up lint and formatting errors in all docs
- [ ] Add CI scripts for backend tests and frontend linting
