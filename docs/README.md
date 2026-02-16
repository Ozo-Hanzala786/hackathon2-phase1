# Todo Web Application

A secure, full-stack todo application with multi-user support and JWT-based authentication.

## Features

- User registration and authentication
- Create, read, update, and delete tasks
- Task completion toggling
- Secure API with JWT authentication
- User isolation - each user can only access their own tasks

## Tech Stack

- **Frontend**: Next.js 16+ with App Router
- **Backend**: FastAPI with Python
- **Database**: PostgreSQL (Neon Serverless)
- **Authentication**: JWT-based with Better Auth principles

## API Endpoints

### Authentication
- `POST /auth/token` - Get access token
- `GET /auth/me` - Get current user info

### Tasks
- `GET /api/{user_id}/tasks` - Get all tasks for user
- `POST /api/{user_id}/tasks` - Create a new task
- `GET /api/{user_id}/tasks/{id}` - Get a specific task
- `PUT /api/{user_id}/tasks/{id}` - Update a task
- `DELETE /api/{user_id}/tasks/{id}` - Delete a task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle task completion

## Security

- JWT-based authentication
- User ID validation in all endpoints
- Data isolation between users
- Protected against unauthorized access

## Running the Application

### Backend
1. Navigate to the `backend/` directory
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables (DATABASE_URL, JWT_SECRET_KEY, etc.)
4. Run the server: `uvicorn src.main:app --reload`

### Frontend
1. Navigate to the `frontend/` directory
2. Install dependencies: `npm install`
3. Run the development server: `npm run dev`