# Quickstart Guide: Console Todo App

## Prerequisites
- Python 3.13 or higher
- UV package manager

## Setup
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv pip install -r requirements.txt
   ```

## Running the Application
```bash
cd src/todo_app/cli
python main.py --help
```

## Basic Usage
- Add a task: `python main.py add --title "Task Title" --description "Task Description"`
- View all tasks: `python main.py list`
- Update a task: `python main.py update --id <task-id> --title "New Title" --description "New Description"`
- Delete a task: `python main.py delete --id <task-id>`
- Mark complete: `python main.py complete --id <task-id>`
- Mark incomplete: `python main.py incomplete --id <task-id>`

## Example Session
```bash
# Add a task
python main.py add --title "Buy groceries" --description "Milk, bread, eggs"

# View all tasks
python main.py list

# Mark task as complete (use the ID from the list command)
python main.py complete --id abc123

# Update a task
python main.py update --id abc123 --title "Buy groceries (done)" --description "Milk, bread, eggs, cheese"
```

## Error Handling
- Invalid commands will display usage information
- Non-existent task IDs will return appropriate error messages
- Empty titles will be rejected with an error message