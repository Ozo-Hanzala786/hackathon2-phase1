# Research: Todo Full-Stack Web Application

**Feature**: 003-todo-web-app | **Date**: 2026-01-21

## Research Summary

This document captures research findings for implementing the full-stack Todo web application with multi-user support, authentication, and data isolation.

## Technology Decisions

### 1. Better Auth Integration

**Decision**: Use Better Auth with JWT session strategy for Next.js 16+ App Router

**Rationale**: Better Auth provides robust authentication with JWT support, integrates well with Next.js App Router, and handles user management automatically.

**Alternatives considered**:
- NextAuth.js - More complex setup for JWT
- Lucia Auth - Less mature ecosystem
- Custom JWT implementation - Higher security risk

### 2. FastAPI JWT Middleware

**Decision**: Implement JWT verification using python-jose with custom dependency injection

**Rationale**: FastAPI's dependency injection system works well with JWT verification, allowing for clean authentication layers that can validate user identity and enforce authorization.

**Alternatives considered**:
- Authlib - More complex for simple JWT validation
- FastAPI-SQLAlchemy with built-in auth - Less flexible for custom validation
- Custom middleware class - Overkill for this use case

### 3. SQLModel Patterns for Data Isolation

**Decision**: Implement user_id as a required field in Task model and enforce filtering at the service layer

**Rationale**: SQLModel with SQLAlchemy provides excellent support for filtering queries by user_id, ensuring data isolation at the database level.

**Alternatives considered**:
- Row-level security in PostgreSQL - More complex setup
- Application-level filtering only - Less secure
- Separate databases per user - Overly complex

### 4. Neon PostgreSQL Connection

**Decision**: Use connection pooling with async drivers for optimal performance with Neon's serverless architecture

**Rationale**: Neon's serverless nature benefits from proper connection management to handle scaling and connection limits effectively.

**Alternatives considered**:
- Direct connections without pooling - Poor performance under load
- Static connection - Not optimal for serverless
- Connection string parameters only - Doesn't address pooling needs

### 5. API Security Patterns

**Decision**: Implement JWT validation at the dependency level in FastAPI, with user_id validation in each route handler

**Rationale**: This provides both authentication (valid JWT) and authorization (user_id matches) in a reusable and maintainable way.

**Alternatives considered**:
- Middleware-only validation - Less granular control
- Decorator-based validation - Harder to test
- Route-level validation only - Repetitive code

## Architecture Patterns

### Frontend-Backend Separation

The application follows a clear separation between frontend and backend responsibilities:
- Frontend: User interface, user experience, API communication
- Backend: Authentication, authorization, data validation, business logic

### Data Flow

1. User authenticates via Better Auth
2. JWT token is stored in browser and sent with API requests
3. Backend validates JWT and extracts user_id
4. Backend verifies user_id in URL matches JWT user_id
5. Backend filters all database queries by user_id
6. Backend returns user-specific data only

## Implementation Considerations

### Error Handling Strategy

- 401 Unauthorized: Invalid or missing JWT
- 403 Forbidden: User ID mismatch between JWT and URL
- 404 Not Found: Resource doesn't exist or doesn't belong to user
- 400 Bad Request: Invalid input data

### Security Measures

1. JWT validation using shared secret from environment
2. User ID validation in all endpoints
3. Database-level filtering by user_id
4. Input validation for all user data
5. Protection against common web vulnerabilities

## Next Steps

Based on this research, the implementation will proceed with:
1. Setting up the project structure with separate frontend/backend
2. Implementing Better Auth integration in Next.js
3. Creating FastAPI backend with JWT middleware
4. Defining SQLModel entities with proper relationships
5. Building the API endpoints with proper authentication/authorization