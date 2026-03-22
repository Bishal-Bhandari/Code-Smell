
# 🚀 AI Code Reviewer SaaS Platform

An AI-powered SaaS platform that automates **Pull Request (PR) reviews** using **static code analysis + LLM-based insights**, built with a production-grade architecture.

---

## 💡 Features

- ✅ Static Code Analysis (AST + Complexity)
- 🤖 AI Code Review (LLM suggestions)
- 🔄 GitHub PR Integration (auto comments)
- 📊 Dashboard for PR analytics
- 🔐 JWT Authentication & API Keys
- 📈 Usage Limits (Free / Pro tiers)
- ⚡ Async Processing with Celery

---

## 🧱 Tech Stack

### Backend
- FastAPI
- Celery + Redis
- MongoDB

### Frontend
- Next.js
- Tailwind CSS

### AI & Analysis
- OpenAI API
- Radon (Cyclomatic Complexity)
- Python AST

### DevOps
- Docker & Docker Compose
- Ngrok (Webhook testing)

---

## 📁 Project Structure

```

backend/
├── analysis_engine/
├── auth/
├── celery_apps/
├── config/
├── db_services/
├── github_service/
├── schemas/
└── main.py

frontend/
docker-compose.yml

````

---

# ⚙️ Setup Instructions

---

## 🔹 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-code-reviewer.git
cd ai-code-reviewer
````

---

## 🔹 2. Backend Setup

### Create Virtual Environment

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

If no requirements file:

```bash
pip install fastapi uvicorn pymongo python-dotenv celery redis passlib[bcrypt] python-jose requests PyGithub radon openai
```

---

## 🔹 3. Environment Variables

Create `.env` inside `backend/`:

```env
OPENAI_API_KEY=your_openai_key
GITHUB_TOKEN=your_github_token
SECRET_KEY=your_secret_key
```

---

## 🔹 4. Run Services (Docker)

From **project root**:

```bash
docker compose up -d
```

This starts:

* MongoDB
* Redis

---

## 🔹 5. Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Access API:

```
http://127.0.0.1:8000/docs
```

---

## 🔹 6. Run Celery Worker

Open new terminal:

```bash
cd backend
celery -A celery_apps.celery_app worker --loglevel=info
```

---

## 🔹 7. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Access frontend:

```
http://localhost:3000
```

---

# 🌐 GitHub Webhook Setup (Ngrok)

---

## 🔹 1. Start Ngrok

```bash
ngrok http 8000
```

Copy URL like:

```
https://abcd1234.ngrok-free.app
```

---

## 🔹 2. Add Webhook in GitHub

Go to:

```
Repo → Settings → Webhooks → Add Webhook
```

Set:

```
Payload URL:
https://YOUR_NGROK_URL/webhook/github

Content type:
application/json

Events:
Pull Request (opened)
```

---

## 🔹 3. Secret (Optional)

Match this in backend:

```python
GITHUB_SECRET = "webhook_secret"
```

---

# 🔄 System Flow

```
GitHub PR Created
        ↓
Webhook Triggered
        ↓
FastAPI Receives Event
        ↓
Celery Task Queued (Redis)
        ↓
Fetch PR Files
        ↓
Static Analysis (AST + Radon)
        ↓
AI Review (LLM)
        ↓
Store Results (MongoDB)
        ↓
Post Comment to GitHub PR
        ↓
Display in Dashboard
```

---

# 🧠 Flow Diagram (Architecture)

```
          ┌───────────────┐
          │   GitHub PR   │
          └──────┬────────┘
                 │ Webhook
                 ▼
        ┌──────────────────┐
        │   FastAPI API    │
        └──────┬───────────┘
               │
               ▼
        ┌───────────────┐
        │   Celery      │
        │   Worker      │
        └──────┬────────┘
               │
   ┌───────────┼────────────┐
   ▼           ▼            ▼
Static     AI Review     GitHub API
Analysis   (LLM)         (Comments)
   │           │            │
   └──────┬────┴────────────┘
          ▼
     MongoDB
          ▼
     Dashboard (Next.js)
```

---

# 🧪 Testing

### API Testing

* Swagger UI → `/docs`

### Auth Testing

* Signup → Login → Use JWT

### Webhook Testing

* Use Ngrok
* Create PR → see logs + comments

---

# 🧩 Key Endpoints

| Endpoint                 | Description    |
| ------------------------ | -------------- |
| POST /auth/signup        | Register user  |
| POST /auth/login         | Login          |
| POST /auth/register-repo | Add repo       |
| GET /dashboard/my-prs    | User PRs       |
| GET /dashboard/analytics | Usage stats    |
| POST /webhook/github     | GitHub webhook |

---

# 🚀 Future Improvements

* Multi-tenant support
* CI/CD pipeline
* Kubernetes deployment
* Advanced ML risk scoring
* Team collaboration features

---

# 👨‍💻 Author

**Bishal Bhandari**

---

# ⭐ If you like this project

Give it a star ⭐ and share feedback!

```
