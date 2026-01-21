"""
Interactive menu system for the Console Todo Application
"""
import sys
from typing import Callable, Dict, Optional
from ..services.task_service import TaskService
from ..utils.validators import validate_task_title


class MenuItem:
    """
    Represents a single menu option with associated action.
    """
    def __init__(self, number: int, label: str, handler: Callable):
        """
        Initialize a menu item.

        Args:
            number: Numeric identifier for the menu option
            label: Display text for the menu option
            handler: Function to execute when selected
        """
        self.number = number
        self.label = label
        self.handler = handler

    def validate(self) -> bool:
        """
        Validate the menu item.

        Returns:
            True if valid, False otherwise
        """
        if not isinstance(self.number, int):
            return False
        if not self.label or not isinstance(self.label, str):
            return False
        if not callable(self.handler):
            return False
        return True


class InteractiveSession:
    """
    Represents the ongoing interactive session with menu navigation and persistent task storage.
    """
    def __init__(self):
        """Initialize the interactive session."""
        self.task_service = TaskService()
        self.is_running = False
        self.menu_options: Dict[int, MenuItem] = {}
        self._setup_menu()

    def _setup_menu(self):
        """Setup the main menu options."""
        self.menu_options = {
            1: MenuItem(1, "Add Task", self._handle_add_task),
            2: MenuItem(2, "List Tasks", self._handle_list_tasks),
            3: MenuItem(3, "Update Task", self._handle_update_task),
            4: MenuItem(4, "Delete Task", self._handle_delete_task),
            5: MenuItem(5, "Mark Task Complete", self._handle_mark_complete),
            6: MenuItem(6, "Mark Task Incomplete", self._handle_mark_incomplete),
            7: MenuItem(7, "Show Help", self._handle_help),
            8: MenuItem(8, "Quit", self._handle_quit),
        }

    def _handle_help(self):
        """Handle displaying help information."""
        print("\n--- Help Information ---")
        print("This is the interactive mode of the Console Todo Application.")
        print("You can perform the following operations:")
        print("1. Add Task: Create a new task with title and description")
        print("2. List Tasks: View all tasks with their completion status")
        print("3. Update Task: Modify the title or description of an existing task")
        print("4. Delete Task: Remove a task from the list")
        print("5. Mark Task Complete: Change a task's status to completed")
        print("6. Mark Task Incomplete: Change a task's status to incomplete")
        print("7. Show Help: Display this help information")
        print("8. Quit: Exit the interactive mode")
        print("\nTask statuses are shown as: [O] for incomplete, [X] for complete")
        print("All tasks are stored in memory only and will be lost when the application exits.\n")

    def display_menu(self):
        """Display the main menu with all available options."""
        print("\n" + "="*50)
        print("Console Todo Application - Interactive Mode")
        print("="*50)
        print()

        for number in sorted(self.menu_options.keys()):
            item = self.menu_options[number]
            print(f"{number}. {item.label}")

        print()

    def _get_user_choice(self) -> Optional[int]:
        """
        Get user's menu choice with validation.

        Returns:
            Selected menu number or None if invalid input
        """
        try:
            choice = input("Enter your choice (1-8): ").strip()
            if not choice:
                print("Error: Please enter a number between 1 and 8\n")
                return None

            choice_num = int(choice)

            if choice_num not in self.menu_options:
                print(f"Error: '{choice}' is not a valid option. Please enter a number between 1 and 8\n")
                return None

            return choice_num
        except ValueError:
            print(f"Error: '{choice}' is not a valid number. Please enter a number between 1 and 8\n")
            return None
        except KeyboardInterrupt:
            print("\n\nReceived interrupt signal. Exiting...")
            self.is_running = False
            return None

    def run(self):
        """Run the interactive session in a continuous loop."""
        print("\n" + "="*50)
        print("Welcome to Console Todo Application - Interactive Mode!")
        print("Perform multiple operations without restarting the application.")
        print("All tasks are stored in memory only and will be lost when exiting.")
        print("="*50 + "\n")

        self.is_running = True

        while self.is_running:
            self.display_menu()

            choice = self._get_user_choice()

            if choice is not None:
                item = self.menu_options[choice]
                try:
                    item.handler()
                except Exception as e:
                    print(f"An error occurred: {str(e)}\n")
            # If choice is None, we either got invalid input or interrupt signal,
            # so we continue the loop or exit based on the signal status

        print("\n" + "="*50)
        print("Goodbye! Thanks for using Console Todo Application.")
        print("Your tasks were stored in memory and have been cleared.")
        print("="*50 + "\n")

    def _handle_add_task(self):
        """Handle adding a new task."""
        print("\n--- Add Task ---")
        title = input("Enter task title: ").strip()

        if not validate_task_title(title):
            print("Error: Task title cannot be empty or whitespace-only\n")
            return

        description = input("Enter task description (optional): ").strip()

        try:
            task = self.task_service.add_task(title, description)
            print(f"Task added successfully!\n")
            self._display_single_task(task)
        except ValueError as e:
            print(f"Error: {str(e)}\n")

    def _handle_list_tasks(self):
        """Handle listing all tasks."""
        print("\n--- List Tasks ---")
        tasks = self.task_service.get_all_tasks()

        if not tasks:
            print("No tasks found.\n")
            return

        print(f"\nYou have {len(tasks)} task(s):\n")
        for task in tasks:
            self._display_single_task(task)
            print()

    def _display_single_task(self, task):
        """Display a single task with clear completion status indicators."""
        status = "X" if task.completed else "O"
        print(f"[{status}] {task.id[:8]} - {task.title}")
        if task.description:
            print(f"      Description: {task.description}")

    def _handle_update_task(self):
        """Handle updating an existing task."""
        print("\n--- Update Task ---")
        task_id = input("Enter task ID to update: ").strip()

        if not task_id:
            print("Error: Task ID cannot be empty\n")
            return

        # Check if task exists
        existing_task = self.task_service.get_task_by_id(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} not found\n")
            return

        print(f"Current task: {existing_task.title}")
        if existing_task.description:
            print(f"Current description: {existing_task.description}")

        new_title = input(f"Enter new title (leave empty to keep '{existing_task.title}'): ").strip()
        new_description = input(f"Enter new description (leave empty to keep current): ").strip()

        # Use existing values if user didn't provide new ones
        if not new_title:
            new_title = existing_task.title
        if not new_description:
            new_description = existing_task.description

        # Validate title if it's being changed
        if new_title != existing_task.title and not validate_task_title(new_title):
            print("Error: Task title cannot be empty or whitespace-only\n")
            return

        try:
            updated_task = self.task_service.update_task(task_id, new_title, new_description)
            if updated_task:
                print("Task updated successfully!\n")
                self._display_single_task(updated_task)
            else:
                print(f"Error: Task with ID {task_id} not found\n")
        except ValueError as e:
            print(f"Error: {str(e)}\n")

    def _handle_delete_task(self):
        """Handle deleting a task."""
        print("\n--- Delete Task ---")
        task_id = input("Enter task ID to delete: ").strip()

        if not task_id:
            print("Error: Task ID cannot be empty\n")
            return

        if self.task_service.delete_task(task_id):
            print(f"Task with ID {task_id} deleted successfully!\n")
        else:
            print(f"Error: Task with ID {task_id} not found\n")

    def _handle_mark_complete(self):
        """Handle marking a task as complete."""
        print("\n--- Mark Task Complete ---")
        task_id = input("Enter task ID to mark complete: ").strip()

        if not task_id:
            print("Error: Task ID cannot be empty\n")
            return

        if self.task_service.mark_complete(task_id):
            print(f"Task with ID {task_id} marked as complete!\n")
            task = self.task_service.get_task_by_id(task_id)
            if task:
                self._display_single_task(task)
        else:
            print(f"Error: Task with ID {task_id} not found\n")

    def _handle_mark_incomplete(self):
        """Handle marking a task as incomplete."""
        print("\n--- Mark Task Incomplete ---")
        task_id = input("Enter task ID to mark incomplete: ").strip()

        if not task_id:
            print("Error: Task ID cannot be empty\n")
            return

        if self.task_service.mark_incomplete(task_id):
            print(f"Task with ID {task_id} marked as incomplete!\n")
            task = self.task_service.get_task_by_id(task_id)
            if task:
                self._display_single_task(task)
        else:
            print(f"Error: Task with ID {task_id} not found\n")

    def _handle_quit(self):
        """Handle quitting the interactive session."""
        self.is_running = False


def run_interactive_mode():
    """Entry point for the interactive mode."""
    try:
        session = InteractiveSession()
        session.run()
    except KeyboardInterrupt:
        print("\n\nReceived interrupt signal. Exiting...")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        sys.exit(1)