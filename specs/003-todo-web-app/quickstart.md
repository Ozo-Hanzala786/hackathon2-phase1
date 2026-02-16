# Quickstart Guide: Todo Full-Stack Web Application

**Feature**: 003-todo-web-app | **Date**: 2026-01-21

## Overview

This guide provides instructions for setting up and running the Todo full-stack web application with multi-user support and authentication.

## Prerequisites

- Node.js 18+ for the frontend
- Python 3.11+ for the backend
- PostgreSQL (or access to Neon Serverless PostgreSQL)
- Better Auth account/credentials (optional for local development)

## Environment Setup

### Backend Environment Variables

Create a `.env` file in the backend directory with the following variables:

```env
DATABASE_URL=postgresql://username:password@localhost:5432/todo_app
BETTER_AUTH_SECRET=your-super-secret-jwt-key-here
BETTER_AUTH_URL=http://localhost:3000
# Add other necessary environment variables
```

### Frontend Environment Variables

Create a `.env.local` file in the frontend directory:

```env
NEXT_PUBLIC_BETTER_AUTH_URL=http://localhost:3000
# Add other necessary environment variables
```

## Installation

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set up the database:
```bash
# Run database migrations
alembic upgrade head
```

4. Start the backend server:
```bash
uvicorn main:app --reload
```

The backend will be available at `http://localhost:8000`.

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`.

## Running the Application

1. Start the backend server (port 8000)
2. Start the frontend server (port 3000)
3. Access the application at `http://localhost:3000`
4. Register a new account or sign in
5. Begin creating and managing tasks

## API Endpoints

Once running, the backend exposes the following authenticated endpoints:

- GET    `/api/{user_id}/tasks` - Get all user's tasks
- POST   `/api/{user_id}/tasks` - Create a new task
- GET    `/api/{user_id}/tasks/{id}` - Get specific task
- PUT    `/api/{user_id}/tasks/{id}` - Update a task
- DELETE `/api/{user_id}/tasks/{id}` - Delete a task
- PATCH  `/api/{user_id}/tasks/{id}/complete` - Toggle completion status

## Testing the Application

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## Troubleshooting

- If authentication fails, verify that the `BETTER_AUTH_SECRET` matches between frontend and backend
- If database connection fails, check that the `DATABASE_URL` is correct
- If API calls return 401/403 errors, ensure JWT token is properly included in requests