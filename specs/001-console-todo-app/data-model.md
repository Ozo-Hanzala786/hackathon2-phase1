# Data Model: Console Todo App

## Task Entity

### Fields
- **id**: Unique identifier for the task (UUID/string)
- **title**: Title of the task (string, required)
- **description**: Description of the task (string, optional)
- **completed**: Boolean indicating completion status (boolean, default: False)

### Validation Rules
- ID must be unique within the task list
- Title must not be empty or whitespace-only
- Description can be empty but not null
- Completed status must be boolean

### State Transitions
- `incomplete` → `complete`: When user marks task as done
- `complete` → `incomplete`: When user marks task as undone

## Task List Collection

### Characteristics
- In-memory storage only (no persistence)
- Maintains order of tasks as added
- Provides lookup by unique ID
- Thread-safe operations (if needed for future extensions)

### Operations Supported
- Add task to collection
- Retrieve all tasks
- Find task by ID
- Update task by ID
- Delete task by ID
- Bulk update completion status