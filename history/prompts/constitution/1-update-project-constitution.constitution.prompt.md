---
id: 1
title: Update Project Constitution
stage: constitution
date: 2026-01-21
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: main
user: hanzala
command: /sp.constitution
labels: [constitution,spec-kit-plus,upgrade,migration]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:
  - none
---

## Prompt

Establish the constitution for a Phase II project that converts a console-based Todo application into a modern, multi-user, full-stack web application using a strict spec-driven, agentic development workflow.

CONSTITUTION RULES:

1. DEVELOPMENT METHODOLOGY (MANDATORY)
- Follow Spec-Kit Plus workflow strictly in this order:
  1) Constitution
  2) Specification
  3) Plan
  4) Tasks
  5) Implementation
- No implementation may begin without an approved specification and plan.
- All code must be generated via Claude Code. Manual coding is strictly prohibited.
- Every code change must trace back to a requirement in the specification and a generated task.

2. TECHNOLOGY CONSTRAINTS
Frontend:
- Use Next.js 16+ with App Router.
- Implement authentication using Better Auth.
- Enable JWT issuance using Better Auth.
- Build a responsive user interface.

Backend:
- Use Python FastAPI.
- Implement RESTful API endpoints.
- Use SQLModel as the ORM.
- Implement JWT verification middleware.

Database:
- Use Neon Serverless PostgreSQL for persistent storage.

3. AUTHENTICATION & SECURITY
- Authentication must be JWT-based.
- Better Auth must issue JWT tokens on user login.
- Frontend must send JWT tokens using the Authorization: Bearer <token> header.
- Backend must verify JWT tokens using a shared secret.
- The shared secret must be provided via environment variables named BETTER_AUTH_SECRET.
- Secrets must never be hard-coded.

4. USER IDENTITY & AUTHORIZATION
- The authenticated user identity must be derived only from the JWT token.
- The user_id provided in API URLs must be validated against the JWT.
- If the user_id in the URL does not match the authenticated user, return 403 Forbidden.
- Requests without valid JWTs must return 401 Unauthorized.

5. DATA ISOLATION
- Enforce strict per-user data isolation.
- Users may only access, modify, or delete their own tasks.
- All database queries must filter by the authenticated user ID.
- Backend enforcement is mandatory; frontend filtering is insufficient.

6. API DESIGN
- Implement the following REST API endpoints:
  GET    /api/{user_id}/tasks
  POST   /api/{user_id}/tasks
  GET    /api/{user_id}/tasks/{id}
  PUT    /api/{user_id}/tasks/{id}
  DELETE /api/{user_id}/tasks/{id}
  PATCH  /api/{user_id}/tasks/{id}/complete
- Use proper HTTP status codes:
  401 Unauthorized
  403 Forbidden
  404 Not Found
  400 Bad Request

7. MONOREPO ORGANIZATION
- Use a single monorepo containing both frontend and backend.
- Keep frontend and backend clearly separated.
- Organize the repository so Claude Code can modify both codebases.

8. QUALITY STANDARDS
- Prefer clarity over cleverness.
- Use production-ready defaults.
- Ensure deterministic and predictable behavior.

9. SUCCESS CRITERIA
- All basic Todo features must work as a web application.
- Multiple users must be supported with strict data isolation.
- Authentication must be enforced on every API request.
- Data must persist in Neon PostgreSQL.
- All development must comply with Spec-Kit Plus methodology.

10. PROHIBITED ACTIONS
- Manual code edits are forbidden.
- Hard-coded secrets are forbidden.
- Backend must not trust frontend for authorization.
- Skipping specification or planning phases is forbidden.

Confirm acceptance of this constitution and enforce it throughout the project lifecycle.

## Response snapshot

Updated the project constitution at .specify/memory/constitution.md to transform from a console-based Todo application to a modern, multi-user, full-stack web application. The new constitution version 2.0.0 establishes principles for:

- Spec-Driven Development Methodology
- Full-Stack Web Application Architecture (Next.js 16+, FastAPI, Neon PostgreSQL)
- JWT-Based Authentication & Security with Better Auth
- User Identity & Authorization Enforcement
- Strict Per-User Data Isolation
- Standardized REST API Design
- Monorepo Organization
- Code Quality and Production Standards

The constitution now enforces the technology stack constraints, authentication requirements, data isolation rules, and API design patterns required for the Phase II project.

## Outcome

- ✅ Impact: Successfully updated constitution from v1.0.0 (console-based) to v2.0.0 (web-based, multi-user) with all required principles
- 🧪 Tests: none
- 📁 Files: Updated .specify/memory/constitution.md with new constitution
- 🔁 Next prompts: Ready to proceed with specification phase using /sp.specify
- 🧠 Reflection: Constitution now properly defines the architectural constraints and development methodology for the full-stack web application transformation

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS - Constitution properly updated with all required principles
- Prompt variant (if applicable): Standard constitution update
- Next experiment (smallest change to try): Proceed with /sp.specify to create feature specification based on new constitution