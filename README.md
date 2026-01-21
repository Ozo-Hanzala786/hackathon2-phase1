# Console Todo Application

A Python console-based todo application that allows users to manage tasks from the command line. All tasks are stored in memory only.

## Features

- Add tasks with titles and descriptions
- View all tasks with clear completion status indicators
- Update existing tasks (modify title and description)
- Delete tasks
- Mark tasks as complete or incomplete

## Prerequisites

- Python 3.13 or higher
- UV package manager (optional, but recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or with UV:
   ```bash
   uv pip install -r requirements.txt
   ```

## Usage

### Adding a Task
```bash
python -m src.todo_app.cli.main add --title "Task Title" --description "Task Description"
```

### Listing All Tasks
```bash
python -m src.todo_app.cli.main list
```

### Updating a Task
```bash
python -m src.todo_app.cli.main update --id <task-id> --title "New Title" --description "New Description"
```

### Deleting a Task
```bash
python -m src.todo_app.cli.main delete --id <task-id>
```

### Marking a Task as Complete
```bash
python -m src.todo_app.cli.main complete --id <task-id>
```

### Marking a Task as Incomplete
```bash
python -m src.todo_app.cli.main incomplete --id <task-id>
```

## Examples

**Note**: All tasks are stored in memory only and will be lost when the application terminates.

### Command-Line Mode

#### Add a task
```bash
python -m src.todo_app.cli.main add --title "Buy groceries" --description "Milk, bread, eggs"
```

#### List all tasks
```bash
python -m src.todo_app.cli.main list
```

#### Update a task
```bash
python -m src.todo_app.cli.main update --id abc123 --title "Buy groceries (updated)" --description "Milk, bread, eggs, cheese"
```

#### Complete a task
```bash
python -m src.todo_app.cli.main complete --id abc123
```

#### Delete a task
```bash
python -m src.todo_app.cli.main delete --id abc123
```

### Interactive Mode

#### Start Interactive Mode
```bash
python -m src.todo_app.cli.main interactive
```

In interactive mode, you can perform multiple operations in a single session without restarting the application. The interactive mode provides a menu-driven interface where you can:
- Add tasks
- List tasks
- Update tasks
- Delete tasks
- Mark tasks as complete/incomplete
- Get help
- Exit the application

All operations in interactive mode maintain the task list in memory during the session.

## Architecture

The application follows a clean architecture with separation of concerns:

- **Models**: Data representation (Task model)
- **Services**: Business logic (TaskService)
- **CLI**: User interface (Command-line interface)
- **Utils**: Helper functions (Validators)

## Testing

To run the unit tests:
```bash
pytest tests/unit/
```

To run all tests:
```bash
pytest tests/
```

## Performance

The application is designed to handle up to 1000 tasks efficiently in memory.