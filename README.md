# Full-stack-AI-ticketing-process-system

An enterprise-level intelligent customer service ticketing system that covers the entire workflow from “order intake → categorization → retrieval → AI initial response → human collaboration → dashboard.”

---

## ✨ Core Features

### User & Ticket Features
- **User management**: Create, list, detail view  
- **Ticket management**: CRUD operations, status updates, priorities, tagging  
- **Ticket replies**: Multi-turn threaded conversations  
- **Filtering & pagination**: Status, priority, requester filtering  
- **Deletion cascade**: Ticket → Replies

### AI Features (In Progress)
- **RAG retrieval** powered by Chroma + SentenceTransformers  
- **AI ticket classification** (automatic labeling)  
- **AI auto-reply** (LLM first response)  
- **Human–AI collaborative editing** (AI suggestions + manual review)  
- **Analytics dashboard** (trends, SLA, satisfaction)

---

## 🧱 Technology Stack

### Backend
- **FastAPI** (Web framework)
- **SQLAlchemy** (ORM)
- **SQLite / PostgreSQL / MySQL** (Databases)
- **Pydantic Settings** (Config)
- **Pytest** (Testing)

### Frontend
- **React 18**
- **Vite**
- **TypeScript**
- **Ant Design**
- **React Context / Zustand** (state management, planned)

### AI / Data Layer
- **Chroma** (Vector database)
- **SentenceTransformers** (Embedding models)
- **LLMs** (OpenAI, DeepSeek, Qwen, Local models)
- **LangChain / LlamaIndex** (RAG framework)

### Infrastructure
- **Docker & Docker Compose**
- **Redis** (optional)
- **Celery + Redis** (optional task queue)

---

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

## API Documentation

### Route Prefix: `/api`

Full API documentation is available via Swagger UI:  
`http://localhost:8000/docs`

---

## Main Endpoints

### User Management

| Method | Path | Description |
|--------|------|-------------|
| POST   | `/api/users`        | Create a user |
| GET    | `/api/users`        | Get user list (supports pagination) |
| GET    | `/api/users/{id}`   | Get user details |

**Example: Create User**
```bash
curl -X POST "http://localhost:8000/api/users" \
  -H "Content-Type: application/json" \
  -d '{"email": "alice@example.com", "name": "Alice"}'
```

#### Ticket Management

| Method | Path                            | Description                                      |
|--------|---------------------------------|--------------------------------------------------|
| POST   | `/api/tickets`                 | Create a ticket                                  |
| GET    | `/api/tickets`                 | Get ticket list (supports filtering & pagination) |
| GET    | `/api/tickets/{id}`            | Get ticket details                               |
| PUT    | `/api/tickets/{id}`            | Update a ticket                                  |
| DELETE | `/api/tickets/{id}`            | Delete a ticket                                  |
| POST   | `/api/tickets/{id}/replies`    | Add a ticket reply                               |
| GET    | `/api/tickets/{id}/replies`    | Get ticket reply list                            |

**Example: Create Ticket**
```bash
curl -X POST "http://localhost:8000/api/tickets" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cannot login",
    "content": "I am unable to login with my account",
    "priority": "high",
    "status": "open",
    "tags": "login,auth",
    "requester_id": 1
  }'
