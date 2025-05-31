# Agent Svelte

A full-stack chat application combining OpenAI-powered agents (Python backend) with a SvelteKit frontend for real-time streaming conversations.

## Overview

This project provides a modern chat interface that connects to an AI agent backend, supporting real-time streaming responses. The architecture consists of:

- **Backend**: Python FastAPI server using OpenAI Agents SDK
- **Frontend**: SvelteKit application with Vercel AI SDK (planned)
- **Features**: Real-time streaming, responsive design, error handling

## Project Structure

```
agent_svelte/
├── agents-python/          # Python backend with OpenAI agent
│   ├── agents_app.py      # FastAPI server with streaming endpoint
│   ├── requirements.txt   # Python dependencies
│   └── tests/            # Backend tests
├── sveltekit/            # SvelteKit frontend (to be created)
└── docs/                 # Documentation
    ├── PRD.md           # Product requirements
    ├── TASK.md          # Implementation tasks
    └── *.md             # Technical documentation
```

## Getting Started

### Backend Setup

1. Navigate to the Python backend:
   ```bash
   cd agents-python
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

5. Run the FastAPI server:
   ```bash
   uvicorn agents_app:app --reload
   ```

   The API will be available at `http://localhost:8000`

### CLI Testing

Test the agent directly from command line:
```bash
python agents_app.py "Your prompt here"
```

### API Endpoints

- **POST** `/api/agent/stream` - Stream agent responses
  - Request body: `{"input": "user message"}` or `{"messages": [...]}`
  - Response: Server-sent events stream

### Frontend Setup

The SvelteKit frontend is planned but not yet implemented. See [docs/TASK.md](docs/TASK.md) for implementation status.

## Development

### Running Tests

```bash
cd agents-python
python -m pytest tests/
```

### Documentation

- [Product Requirements](docs/PRD.md) - Project objectives and requirements
- [Task List](docs/TASK.md) - Implementation progress
- [Agent SDK Guide](docs/agent-sdk.md) - OpenAI Agents SDK documentation
- [Streaming Integration](docs/streaming-integration.md) - Streaming implementation details
- [SvelteKit AI SDK](docs/sveltekit-ai-sdk.md) - Frontend integration guide

## Tech Stack

- **Backend**: Python, FastAPI, OpenAI Agents SDK
- **Frontend** (planned): SvelteKit v5, Vercel AI SDK, Tailwind CSS + DaisyUI
- **Real-time**: Server-sent events for streaming responses

## Contributing

1. Check the [task list](docs/TASK.md) for current progress
2. Follow existing code patterns and conventions
3. Run tests before submitting changes
4. Update documentation as needed

## License

MIT