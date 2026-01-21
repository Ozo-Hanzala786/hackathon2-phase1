"""
Unit tests for Interactive Menu functionality
"""
import pytest
from unittest.mock import patch, MagicMock
from src.todo_app.cli.interactive_menu import InteractiveSession, MenuItem


def test_menu_item_creation():
    """Test creating a MenuItem with valid data."""
    mock_handler = MagicMock()
    item = MenuItem(1, "Test Label", mock_handler)

    assert item.number == 1
    assert item.label == "Test Label"
    assert item.handler == mock_handler


def test_menu_item_validation_success():
    """Test MenuItem validation with valid data."""
    mock_handler = MagicMock()
    item = MenuItem(1, "Test Label", mock_handler)

    assert item.validate() is True


def test_menu_item_validation_failure_number():
    """Test MenuItem validation with invalid number."""
    mock_handler = MagicMock()
    item = MenuItem("invalid", "Test Label", mock_handler)

    assert item.validate() is False


def test_menu_item_validation_failure_label():
    """Test MenuItem validation with invalid label."""
    mock_handler = MagicMock()
    item = MenuItem(1, "", mock_handler)

    assert item.validate() is False


def test_menu_item_validation_failure_handler():
    """Test MenuItem validation with invalid handler."""
    item = MenuItem(1, "Test Label", "not_callable")

    assert item.validate() is False


def test_interactive_session_initialization():
    """Test initializing an InteractiveSession."""
    session = InteractiveSession()

    assert session.task_service is not None
    assert session.is_running is False
    assert len(session.menu_options) == 8  # 8 menu options


def test_interactive_session_menu_setup():
    """Test that InteractiveSession sets up all menu options."""
    session = InteractiveSession()

    expected_options = {1, 2, 3, 4, 5, 6, 7, 8}
    actual_options = set(session.menu_options.keys())

    assert actual_options == expected_options
    assert session.menu_options[1].label == "Add Task"
    assert session.menu_options[2].label == "List Tasks"
    assert session.menu_options[8].label == "Quit"


@patch('builtins.input', side_effect=['2', '8'])  # Choose 'List Tasks' then 'Quit'
@patch('sys.stdout', new_callable=lambda: type('MockStdOut', (), {'write': lambda self, s: None})())
def test_interactive_session_run_flow(mock_stdout, mock_input):
    """Test the interactive session run flow."""
    session = InteractiveSession()
    # Override the display methods to avoid actual printing during test
    session.display_menu = lambda: None

    # Mock the handler methods
    original_handlers = {}
    for num, item in session.menu_options.items():
        original_handlers[num] = item.handler
        if num == 2:  # List Tasks
            item.handler = lambda: print("Tasks listed")
        elif num == 8:  # Quit
            item.handler = lambda: setattr(session, 'is_running', False)

    # Run the session
    session.is_running = True
    choice = session._get_user_choice()
    assert choice == 2  # First choice should be 2 (List Tasks)

    # Restore original handlers
    for num, handler in original_handlers.items():
        session.menu_options[num].handler = handler


def test_interactive_session_shared_task_service():
    """Test that InteractiveSession maintains shared task service across operations."""
    session = InteractiveSession()

    # Add a task
    task = session.task_service.add_task("Test Task", "Test Description")

    # Verify the task exists in the session's task service
    tasks = session.task_service.get_all_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Test Task"
    assert tasks[0].description == "Test Description"