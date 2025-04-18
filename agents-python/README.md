# Python Agent Backend

This directory contains the Python text-only agent backend.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in this directory with your OpenAI key:
   ```bash
   echo "OPENAI_API_KEY=your_openai_key" > .env
   ```

4. Run the FastAPI server:
   ```bash
   uvicorn agents_app:app --reload --host 0.0.0.0 --port 8000
   ```

5. Use the CLI:
   ```bash
   python agents_app.py "Your prompt here"
   ```

## API Endpoint

- **SSE Stream**: `http://localhost:8000/api/agent/stream`
