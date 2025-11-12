# Full-stack-AI-ticketing-process-system

An enterprise-level intelligent customer service ticketing system that covers the entire workflow from “order intake → categorization → retrieval → AI initial response → human collaboration → dashboard.”

## Project Structure
```
.
├── backend/          # FastAPI app, configuration, and health check examples
├── frontend/         # Vite + React + Ant Design console scaffold
├── infra/            # docker-compose setup to launch frontend + backend + Chroma
├── scripts/          # Environment initialization scripts
├── docs/             # Architecture documentation
├── outline.md        # Outline
└── AGENTS.md         # Repository collaboration guidelines
```

## Quick Start
1. **Install dependencies**
   ```bash
   make bootstrap
   ```
2. **Start the FastAPI backend**
   ```bash
   make run-backend
   ```
3. **Start the React frontend**
   ```bash
   make run-frontend
   ```
4. **Launch the full stack (optional)**
   ```bash
   make dev-up
   ```
   > On first run, this will execute `npm install` inside the container (requires network access to NPM). Once completed, the frontend, backend, and Chroma will all start simultaneously.

Visit `http://localhost:8000/health` to verify the API, or open `http://localhost:5173` in your browser to view the interface.

## Architecture Overview
- **Frontend**：Displays course milestones and tech stack cards; serves as the container for the upcoming Ticket UI.
- **Backend**：FastAPI provides system health checks and will soon expose ticket APIs; configuration is injected via `.env`.
- **Chroma**：Pre-launched by Docker and ready to receive embedded vectors.
- **LLM Interface**：Not yet connected; can be enabled via environment variables.