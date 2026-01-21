# Python Console Todo Application Constitution

## Core Principles

### In-Memory Storage Only
All tasks exist only in memory during runtime; No persistence to files, databases, or external storage systems; Strictly limited to in-memory operations to maintain simplicity and phase I scope

### Console Interface Only
Interface is strictly command-line/terminal based; No GUI, web interfaces, or APIs; Output must be clear and user-friendly for terminal consumption

### Five Basic Features Only
Implement exactly five features: Add task, View tasks, Update task, Delete task, Mark complete/incomplete; No additional features beyond these core requirements; Adhere strictly to Phase I scope

### Clean Code and Minimal Abstractions
Follow clean code principles with clear, descriptive naming; Keep functions small and single-purpose; Avoid unnecessary abstractions; Do not include unused code or speculative features

### Python 3.13 and UV Environment
Language must be Python 3.13 or higher; Environment uses UV package manager; Follow modern Python standards and conventions

### Error Handling and Input Validation
Invalid input must be handled gracefully; Non-existent IDs, empty fields, and malformed input must result in clear error messages; No crashes on invalid user input

## Technology Constraints and Code Quality
Language: Python 3.13+, Environment: UV, Interface: Console/terminal only, Tooling: Claude Code and Spec-Kit Plus, Code quality: Clean code principles, descriptive naming, small functions, avoid unnecessary abstractions

## Development Workflow
Specification → Plan → Tasks → Implementation workflow must be followed in exact order; No code until specification is completed and approved; Every implementation must trace back to a written task; Implement features incrementally according to task list; Do not modify unrelated files during a task

## Governance
Constitution supersedes all other practices; Amendments require documentation and approval; All implementations must comply with the five basic features constraint; Changes must not exceed Phase I scope; Specification-first approach must be maintained

**Version**: 1.0.0 | **Ratified**: 2026-01-16 | **Last Amended**: 2026-01-16