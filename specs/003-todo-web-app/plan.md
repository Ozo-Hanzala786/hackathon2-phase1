# Implementation Plan: Todo Full-Stack Web Application

**Branch**: `003-todo-web-app` | **Date**: 2026-01-21 | **Spec**: specs/003-todo-web-app/spec.md
**Input**: Feature specification from `/specs/003-todo-web-app/spec.md`

## Summary

Implementation of a full-stack web-based Todo application with multi-user support, authentication, and data isolation. The system will use Next.js 16+ for the frontend, FastAPI for the backend, and Neon PostgreSQL for data persistence, with Better Auth providing JWT-based authentication.

## Technical Context

**Language/Version**: Python 3.11+ for backend, JavaScript/TypeScript for frontend Next.js 16+
**Primary Dependencies**: Next.js, Better Auth, FastAPI, SQLModel, Neon PostgreSQL driver
**Storage**: Neon Serverless PostgreSQL for persistent storage
**Testing**: pytest for backend, Jest/React Testing Library for frontend
**Target Platform**: Web application accessible via browsers
**Project Type**: Full-stack web application with separate frontend and backend
**Performance Goals**: <1 second response time for task operations, <2 minute user registration/auth
**Constraints**: <100ms p95 for internal API calls, proper security implementation with JWT, data isolation between users
**Scale/Scope**: Multi-user support with individual task lists, secure authentication

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- ✅ Spec-Driven Development: Following Constitution → Specification → Plan → Tasks → Implementation
- ✅ Full-Stack Architecture: Using Next.js 16+ with App Router for frontend, FastAPI for backend
- ✅ JWT Authentication: Implementing Better Auth with JWT issuance and verification
- ✅ Data Isolation: Enforcing per-user data isolation in all database queries
- ✅ REST API Design: Implementing required endpoints with proper HTTP status codes
- ✅ Monorepo Organization: Separating frontend and backend in clear directory structure
- ✅ Security: No hard-coded secrets, using environment variables for BETTER_AUTH_SECRET

## Project Structure

### Documentation (this feature)
```text
specs/003-todo-web-app/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)
```text
backend/
├── src/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── task.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── task_service.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── deps.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── auth.py
│   │       └── tasks.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── security.py
│   └── main.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── contract/
├── requirements.txt
└── alembic/

frontend/
├── src/
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx
│   │   ├── login/
│   │   ├── signup/
│   │   └── dashboard/
│   ├── components/
│   ├── lib/
│   │   └── auth.ts
│   └── services/
│       └── api.ts
├── package.json
├── next.config.js
└── .env.local

database/
├── schemas/
│   └── schema.sql
└── migrations/
```

**Structure Decision**: Selected Option 2: Web application with separate backend and frontend directories to maintain clear separation of concerns while enabling coordinated development.

## Phase 0: Research & Unknowns Resolution

### Research Tasks

1. **Better Auth Integration**: Research how to properly integrate Better Auth with Next.js App Router and configure JWT issuance
2. **FastAPI JWT Middleware**: Research implementation of JWT verification middleware in FastAPI
3. **SQLModel Best Practices**: Research optimal patterns for implementing user-task relationships with proper filtering
4. **Neon PostgreSQL Connection**: Research best practices for connecting to Neon Serverless PostgreSQL from FastAPI
5. **Cross-User Data Isolation**: Research patterns for enforcing data isolation at the database level

## Phase 1: Design & Contracts

### Data Model Design

Based on the specification, the system will implement two main entities:

- **User**: Authentication identifier from Better Auth
- **Task**: With id, title, optional description, completed status, and timestamps; linked to User

### API Contract Design

Following the specification, the backend will expose these endpoints:

- GET    /api/{user_id}/tasks - Retrieve all tasks for authenticated user
- POST   /api/{user_id}/tasks - Create a new task for authenticated user
- GET    /api/{user_id}/tasks/{id} - Retrieve specific task details
- PUT    /api/{user_id}/tasks/{id} - Update task details
- DELETE /api/{user_id}/tasks/{id} - Delete a task
- PATCH  /api/{user_id}/tasks/{id}/complete - Toggle completion status

All endpoints will enforce JWT authentication and user ID validation.

### Quickstart Guide

1. Clone the repository
2. Set up environment variables (DATABASE_URL, BETTER_AUTH_SECRET)
3. Install backend dependencies: `pip install -r requirements.txt`
4. Install frontend dependencies: `npm install`
5. Run database migrations
6. Start backend: `uvicorn main:app --reload`
7. Start frontend: `npm run dev`
8. Access the application at http://localhost:3000

## Phase 2: Task Planning

Tasks will be generated in `/specs/003-todo-web-app/tasks.md` via the `/sp.tasks` command based on this plan, research findings, and data models.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| None      | None       | None                                |
