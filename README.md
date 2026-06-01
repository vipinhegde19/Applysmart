# ApplySmart — AI-Powered Job Application Tracker

A full-stack REST API built with Python and FastAPI that helps job seekers track applications and leverage AI to improve their job search.

## Features

- **Job Tracking** — Add, update, and manage all job applications in one place
- **JWT Authentication** — Secure user registration and login
- **AI Resume Tailor** — Paste a job description and get AI-rewritten resume bullets
- **AI Interview Prep** — Generate likely interview questions based on JD and resume

## Tech Stack

- **Backend** — Python, FastAPI
- **Database** — PostgreSQL, SQLAlchemy ORM
- **Authentication** — JWT tokens, bcrypt password hashing
- **AI** — Groq LLaMA 3.3 API
- **Tools** — Git, Postman, VS Code

## API Endpoints

### Auth
- `POST /auth/register` — Register a new user
- `POST /auth/login` — Login and receive JWT token

### Jobs
- `GET /jobs/` — Get all job applications
- `POST /jobs/` — Add a new job application
- `GET /jobs/{id}` — Get a specific job
- `PUT /jobs/{id}` — Update a job
- `DELETE /jobs/{id}` — Delete a job
- `POST /jobs/{id}/tailor-resume` — AI resume tailoring
- `POST /jobs/{id}/interview-questions` — AI interview prep

## Setup

```bash
# Clone the repository
git clone https://github.com/vipinhegde19/Applysmart.git

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your credentials
DATABASE_URL=postgresql://postgres:password@localhost:5432/applysmart
SECRET_KEY=your_secret_key
ALGORITHM=HS256
GROQ_API_KEY=your_groq_api_key

# Run the server
uvicorn app.main:app --reload
```

## Author

Vipin Hegde — [LinkedIn](https://linkedin.com/in/vipin-hegde) | [GitHub](https://github.com/vipinhegde19)
