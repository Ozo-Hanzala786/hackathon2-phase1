# Data Model: Todo Full-Stack Web Application

**Feature**: 003-todo-web-app | **Date**: 2026-01-21

## Overview

This document defines the data models for the full-stack Todo web application with multi-user support and data isolation.

## Entity Definitions

### User Entity

**Description**: Represents an authenticated user in the system. The user identity is derived from the JWT token issued by Better Auth.

**Fields**:
- `id` (string): Unique identifier from Better Auth JWT token (primary identifier)
- `email` (string, optional): User's email address (for identification purposes)
- `created_at` (datetime): Timestamp when user account was registered
- `updated_at` (datetime): Timestamp when user account was last updated

**Relationships**:
- One-to-Many: User has many Tasks

**Notes**:
- The `id` field comes from the authenticated JWT and is not stored in our database
- User authentication is handled by Better Auth
- All tasks are associated with the user's JWT-derived ID

### Task Entity

**Description**: Represents a todo item created and managed by a specific user.

**Fields**:
- `id` (UUID/int): Primary key, unique identifier for the task
- `title` (string): Title of the task (required, max 255 characters)
- `description` (string, optional): Detailed description of the task (max 1000 characters)
- `completed` (boolean): Whether the task is completed (default: false)
- `user_id` (string): Foreign key linking to the user who owns this task
- `created_at` (datetime): Timestamp when task was created
- `updated_at` (datetime): Timestamp when task was last updated

**Validation Rules**:
- `title`: Required, minimum 1 character, maximum 255 characters
- `description`: Optional, maximum 1000 characters
- `user_id`: Required, must match the authenticated user's ID from JWT
- `completed`: Boolean, default to false

**Relationships**:
- Many-to-One: Task belongs to one User (via user_id foreign key)

**State Transitions**:
- `completed` field can transition from `false` to `true` or `true` to `false` via PATCH /complete endpoint

## Database Schema

### Tasks Table
```
tasks
├── id (UUID/INT, PRIMARY KEY, AUTO_INCREMENT)
├── title (VARCHAR(255), NOT NULL)
├── description (TEXT, NULL)
├── completed (BOOLEAN, DEFAULT false)
├── user_id (VARCHAR(255), NOT NULL, FOREIGN KEY reference to user's JWT ID)
├── created_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP)
└── updated_at (TIMESTAMP, DEFAULT CURRENT_TIMESTAMP ON UPDATE)
```

## Access Control

All database queries must include a WHERE clause filtering by `user_id` to ensure data isolation between users. This is enforced at both the application and database levels.

## Indexes

- Primary key index on `id`
- Index on `user_id` for efficient filtering of user-specific tasks
- Composite index on `user_id` and `completed` for efficient filtering by both user and completion status