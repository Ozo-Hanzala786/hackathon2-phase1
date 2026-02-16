<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 2.0.0
Modified principles: All principles were replaced to reflect transition from Phase I (console-based) to Phase II (web-based, multi-user)
Added sections: New technology stack, authentication & security, data isolation, API design, monorepo organization
Removed sections: Console-specific and in-memory storage principles
Templates requiring updates: ✅ Updated .specify/templates/plan-template.md, .specify/templates/spec-template.md, .specify/templates/tasks-template.md
Follow-up TODOs: None
-->

# Modern Multi-User Web Todo Application Constitution

## Core Principles

### Spec-Driven Development Methodology
Follow Spec-Kit Plus workflow strictly in this order: Constitution → Specification → Plan → Tasks → Implementation; No implementation may begin without an approved specification and plan; All code must be generated via Claude Code with manual coding strictly prohibited; Every code change must trace back to a requirement in the specification and a generated task

### Full-Stack Web Application Architecture
Frontend: Use Next.js 16+ with App Router for modern web interface; Implement authentication using Better Auth with JWT issuance; Build a responsive user interface that works across devices
Backend: Use Python FastAPI for RESTful API endpoints; Use SQLModel as the ORM for database operations; Implement JWT verification middleware for security
Database: Use Neon Serverless PostgreSQL for persistent storage of user data

### JWT-Based Authentication & Security
Authentication must be JWT-based using Better Auth; Better Auth must issue JWT tokens on user login; Frontend must send JWT tokens using the Authorization: Bearer <token> header; Backend must verify JWT tokens using a shared secret provided via BETTER_AUTH_SECRET environment variable; Secrets must never be hard-coded and must be managed via environment variables only

### User Identity & Authorization Enforcement
The authenticated user identity must be derived only from the JWT token; The user_id provided in API URLs must be validated against the JWT; If the user_id in the URL does not match the authenticated user, return 403 Forbidden; Requests without valid JWTs must return 401 Unauthorized; Backend enforcement of authorization is mandatory and cannot rely on frontend filtering

### Strict Per-User Data Isolation
Enforce strict per-user data isolation in all database queries; Users may only access, modify, or delete their own tasks; All database queries must filter by the authenticated user ID; Backend enforcement is mandatory; Frontend filtering is insufficient for security; Data must persist securely in Neon PostgreSQL with proper access controls

### Standardized REST API Design
Implement the following REST API endpoints: GET /api/{user_id}/tasks, POST /api/{user_id}/tasks, GET /api/{user_id}/tasks/{id}, PUT /api/{user_id}/tasks/{id}, DELETE /api/{user_id}/tasks/{id}, PATCH /api/{user_id}/tasks/{id}/complete; Use proper HTTP status codes: 401 Unauthorized, 403 Forbidden, 404 Not Found, 400 Bad Request; Maintain consistent API design patterns across all endpoints

### Monorepo Organization
Use a single monorepo containing both frontend and backend applications; Keep frontend and backend clearly separated with distinct directories and configurations; Organize the repository structure so Claude Code can modify both codebases efficiently; Maintain clear separation of concerns while enabling coordinated development

### Code Quality and Production Standards
Prefer clarity over cleverness in all implementations; Use production-ready defaults for security, performance, and reliability; Ensure deterministic and predictable behavior in all components; Maintain clean code principles with descriptive naming and well-documented functionality

## Technology Constraints and Code Quality
Frontend: Next.js 16+, App Router, Better Auth; Backend: Python FastAPI, SQLModel ORM, JWT middleware; Database: Neon Serverless PostgreSQL; Environment: Claude Code and Spec-Kit Plus; Code quality: Production-ready defaults, clear documentation, testable components

## Development Workflow
Specification → Plan → Tasks → Implementation workflow must be followed in exact order; No implementation until specification and plan are completed and approved; Every implementation must trace back to a written task; Implement features incrementally according to task list; Do not modify unrelated files during a task; Maintain strict adherence to architectural constraints defined in this constitution

## Governance
Constitution supersedes all other practices; Amendments require documentation and approval; All implementations must comply with full-stack web application requirements; Changes must follow Phase II scope; Specification-first approach must be maintained; Manual code edits are forbidden; Hard-coded secrets are forbidden; Backend must not trust frontend for authorization

**Version**: 2.0.0 | **Ratified**: 2026-01-21 | **Last Amended**: 2026-01-21
