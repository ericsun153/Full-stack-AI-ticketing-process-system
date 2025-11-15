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

## 🚀 Local Development

### 1. Install dependencies

```bash
make bootstrap
```

This command creates a Python virtual environment, installs backend and frontend dependencies.

---

### 2. Configure environment variables

```bash
cd backend
cp .env.example .env
```

Modify `.env` as needed.

---

### 3. Start backend service

```bash
make run-backend
```

Backend endpoints:  
- API root → http://localhost:8000  
- Swagger → http://localhost:8000/docs  
- Health check → http://localhost:8000/health  

---

### 4. Start frontend service (new terminal)

```bash
make run-frontend
```

Frontend pages:  
- Home: http://localhost:5173/  
- Ticket list: http://localhost:5173/tickets  
- Create ticket: http://localhost:5173/tickets/new  
- Ticket detail: http://localhost:5173/tickets/{id}

---

### 5. Full-stack start using Docker

```bash
make dev-up
```

Stop with:

```bash
make dev-down
```

---

## Architecture Overview
- **Frontend**：Displays course milestones and tech stack cards; serves as the container for the upcoming Ticket UI.
- **Backend**：FastAPI provides system health checks and will soon expose ticket APIs; configuration is injected via `.env`.
- **Chroma**：Pre-launched by Docker and ready to receive embedded vectors.
- **LLM Interface**：Not yet connected; can be enabled via environment variables.

## 🎨 Frontend Features

### Ticket List Page (`/tickets`)
- Table view (ID, title, status, priority, tags, created time)  
- Filters: status, priority  
- Pagination  
- Color-coded tags  
- Clickable details  
- Buttons: **New Ticket**, **Refresh**

### Create Ticket Page (`/tickets/new`)
- Fields:
  - title (required)
  - content (required)
  - requester (dropdown)
  - status (default Open)
  - priority (default Medium)
  - tags (comma-separated)
- Real-time validation  
- Redirect to detail page after creation  
- Error handling for invalid requester  

### Ticket Detail Page (`/tickets/{id}`)
#### View:
- Ticket info  
- Replies in chronological order  
- Requester and reply authors

#### Edit:
- Editable modal  
- Partial update allowed  
- Auto refresh  

#### Delete:
- Confirmation modal  
- Cascade delete replies  

#### Reply:
- Choose reply author  
- Enter content  
- Auto refresh reply list  

---

## 📡 API Documentation

### Route Prefix: `/api`

Swagger UI → http://localhost:8000/docs

---

### User Management API

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/users` | Create user |
| GET | `/api/users` | List users |
| GET | `/api/users/{id}` | User details |

### Example: Create User

```bash
curl -X POST "http://localhost:8000/api/users" \
  -H "Content-Type: application/json" \
  -d '{"email": "alice@example.com", "name": "Alice"}'
```

---

### Ticket Management API

| Method | Path | Description |
|--------|------|-------------|
| POST | `/api/tickets` | Create ticket |
| GET | `/api/tickets` | List tickets (filters + pagination) |
| GET | `/api/tickets/{id}` | Ticket details |
| PUT | `/api/tickets/{id}` | Update ticket |
| DELETE | `/api/tickets/{id}` | Delete ticket |
| POST | `/api/tickets/{id}/replies` | Add reply |
| GET | `/api/tickets/{id}/replies` | List replies |

### Example: Create Ticket

```bash
curl -X POST "http://localhost:8000/api/tickets" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cannot login",
    "content": "I am unable to login",
    "priority": "high",
    "status": "open",
    "tags": "login,auth",
    "requester_id": 1
  }'
```

### Filtering Example

```bash
GET /api/tickets?page=1&page_size=20&status=open&priority=high&requester_id=1
```

### Update Ticket Example

```bash
curl -X PUT "http://localhost:8000/api/tickets/1" \
  -H "Content-Type: application/json" \
  -d '{"status": "in_progress"}'
```

---

## 📘 Data Models

### User
- id  
- email  
- name  
- created_at  

### Ticket
- id  
- title  
- content  
- status  
- priority  
- tags  
- requester_id  
- created_at  
- updated_at  

### Reply
- id  
- ticket_id  
- author_id  
- content  
- created_at  

---

## 🧪 Testing

### Backend tests

```bash
make test-backend
```

Or:

```bash
cd backend && pytest tests/ -v
```

Test coverage:
- User CRUD  
- Ticket CRUD  
- Filtering + pagination  
- Replies  
- Cascade delete  
- Foreign key validation  

Test file:

```bash
backend/tests/test_tickets_crud.py
```

---

### Frontend testing

```bash
cd frontend && npm run dev
```

```bash
cd frontend && npm run build
```

```bash
cd frontend && npm run lint
```

---

## 🛠 Developer Guide

### Common Commands

```bash
make bootstrap
make run-backend
make run-frontend
make dev-up
make dev-down
make dev-logs
make test-backend
make lint
make format
```

---

## ⚙ Environment Variables

```bash
# Database configuration
DATABASE_URL=sqlite+aiosqlite:///./astratickets.db

# Vector store
VECTOR_STORE_PATH=./vector_store

# LLM (optional)
# OPENAI_API_KEY=sk-...
# LLM_PROVIDER=openai
```

---

## Deployment

### Docker Compose (Recommended)

```bash
docker compose -f infra/docker-compose.yml up -d
```

---

## Production Deployment

### 1. Backend Deployment

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

---

### 2. Frontend Deployment

```bash
cd frontend
npm install
npm run build
# Deploy the dist/ folder to a static web server (Nginx, Caddy, etc.)
```

---

### 3. Database: Switch to PostgreSQL or MySQL

Edit `backend/.env`:

```bash
DATABASE_URL=postgresql://user:password@localhost:5432/astratickets
```