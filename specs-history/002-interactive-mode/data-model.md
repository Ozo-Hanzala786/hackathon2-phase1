# Data Model: Interactive Mode

## InteractiveSession Entity

### Fields
- **task_service**: Instance of TaskService to maintain tasks during the session (TaskService object)
- **is_running**: Boolean indicating if the interactive session is active (boolean, default: True)
- **menu_options**: Dictionary mapping menu numbers to function handlers (dict)

### State Transitions
- `running` → `exited`: When user selects quit option or sends interrupt signal
- `idle` → `processing`: When user selects a menu option
- `processing` → `idle`: After operation completes, returns to main menu

## MenuItem Entity

### Fields
- **number**: Numeric identifier for the menu option (int)
- **label**: Display text for the menu option (string)
- **handler**: Function to execute when selected (callable)

### Validation Rules
- Menu numbers must be unique within the session
- Labels must be non-empty strings
- Handlers must be callable functions