# Quickstart Guide: Interactive Mode

## Prerequisites
- Python 3.13 or higher
- Existing console todo application installed

## Setup
1. Ensure the base console todo application is properly installed
2. Navigate to the project directory
3. Install dependencies if not already installed:
   ```bash
   pip install -r requirements.txt
   ```

## Running Interactive Mode
The interactive mode is integrated into the main application. To start:

```bash
python -m src.todo_app.cli.main interactive
```

Or if a dedicated command is implemented:
```bash
python -m src.todo_app.cli.interactive_menu
```

## Using Interactive Mode
Once in interactive mode, you'll see a menu like this:

```
Console Todo Application - Interactive Mode
==========================================

1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Quit

Enter your choice (1-7):
```

## Example Session
```
Console Todo Application - Interactive Mode
==========================================

1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Quit

Enter your choice (1-7): 1
Enter task title: Buy groceries
Enter task description (optional): Milk, bread, eggs
Task added successfully!

Console Todo Application - Interactive Mode
==========================================

1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Quit

Enter your choice (1-7): 2

You have 1 task(s):

[X] abc12345 - Buy groceries
      Description: Milk, bread, eggs

Console Todo Application - Interactive Mode
==========================================

1. Add Task
2. List Tasks
3. Update Task
4. Delete Task
5. Mark Task Complete
6. Mark Task Incomplete
7. Quit

Enter your choice (1-7): 7
Goodbye!
```

## Error Handling
- Invalid menu choices will show an error message and return to the main menu
- Invalid task IDs will show appropriate error messages
- Empty titles will be rejected with error messages
- The application will not crash on invalid input; it will prompt again