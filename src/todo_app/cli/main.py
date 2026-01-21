#!/usr/bin/env python3
"""
Main CLI entry point for the Console Todo Application
"""
import argparse
import sys
import logging
from typing import Optional
from ..services.task_service import TaskService
from ..utils.validators import validate_task_title

# Import the interactive mode functionality
from .interactive_menu import run_interactive_mode

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def display_task(task):
    """Display a single task with clear completion status indicators."""
    status = "X" if task.completed else "O"
    print(f"[{status}] {task.id[:8]} - {task.title}")
    if task.description:
        print(f"      Description: {task.description}")


def display_tasks(tasks):
    """Display all tasks with clear completion status indicators."""
    if not tasks:
        print("No tasks found.")
        return

    print(f"\nYou have {len(tasks)} task(s):\n")
    for task in tasks:
        display_task(task)
        print()


def main():
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(description='Console Todo Application')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Add task command
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('--title', required=True, help='Title of the task')
    add_parser.add_argument('--description', required=False, default="", help='Description of the task')

    # List tasks command
    list_parser = subparsers.add_parser('list', help='List all tasks')

    # Update task command
    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('--id', required=True, help='ID of the task to update')
    update_parser.add_argument('--title', required=False, help='New title of the task')
    update_parser.add_argument('--description', required=False, help='New description of the task')

    # Delete task command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('--id', required=True, help='ID of the task to delete')

    # Mark task as complete command
    complete_parser = subparsers.add_parser('complete', help='Mark a task as complete')
    complete_parser.add_argument('--id', required=True, help='ID of the task to mark complete')

    # Mark task as incomplete command
    incomplete_parser = subparsers.add_parser('incomplete', help='Mark a task as incomplete')
    incomplete_parser.add_argument('--id', required=True, help='ID of the task to mark incomplete')

    # Interactive mode command
    subparsers.add_parser('interactive', help='Run the application in interactive mode')

    # Parse arguments
    args = parser.parse_args()

    # Handle interactive mode separately
    if args.command == 'interactive':
        run_interactive_mode()
        return

    # Initialize the task service
    task_service = TaskService()

    # Handle other commands
    if args.command == 'add':
        logger.info(f"Adding task with title: {args.title}")
        try:
            # Validate input
            if not validate_task_title(args.title):
                logger.error("Invalid task title provided")
                print("Error: Task title cannot be empty or whitespace-only", file=sys.stderr)
                sys.exit(1)

            # Add the task
            task = task_service.add_task(args.title, args.description)
            logger.info(f"Task added successfully with ID: {task.id}")
            print(f"Task added successfully!")
            display_task(task)
        except ValueError as e:
            logger.error(f"Error adding task: {e}")
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == 'list':
        logger.info("Listing all tasks")
        tasks = task_service.get_all_tasks()
        display_tasks(tasks)
    elif args.command == 'update':
        logger.info(f"Updating task with ID: {args.id}")
        try:
            # Validate task ID
            if not args.id or not args.id.strip():
                logger.error("Invalid task ID provided")
                print("Error: Task ID cannot be empty", file=sys.stderr)
                sys.exit(1)

            # Update the task
            updated_task = task_service.update_task(args.id, args.title, args.description)
            if updated_task:
                logger.info(f"Task updated successfully with ID: {updated_task.id}")
                print("Task updated successfully!")
                display_task(updated_task)
            else:
                logger.warning(f"Task with ID {args.id} not found")
                print(f"Error: Task with ID {args.id} not found", file=sys.stderr)
                sys.exit(1)
        except ValueError as e:
            logger.error(f"Error updating task: {e}")
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
    elif args.command == 'delete':
        logger.info(f"Deleting task with ID: {args.id}")
        # Validate task ID
        if not args.id or not args.id.strip():
            logger.error("Invalid task ID provided")
            print("Error: Task ID cannot be empty", file=sys.stderr)
            sys.exit(1)

        # Delete the task
        if task_service.delete_task(args.id):
            logger.info(f"Task deleted successfully with ID: {args.id}")
            print(f"Task with ID {args.id} deleted successfully!")
        else:
            logger.warning(f"Task with ID {args.id} not found")
            print(f"Error: Task with ID {args.id} not found", file=sys.stderr)
            sys.exit(1)
    elif args.command == 'complete':
        logger.info(f"Marking task as complete with ID: {args.id}")
        # Validate task ID
        if not args.id or not args.id.strip():
            logger.error("Invalid task ID provided")
            print("Error: Task ID cannot be empty", file=sys.stderr)
            sys.exit(1)

        # Mark task as complete
        if task_service.mark_complete(args.id):
            logger.info(f"Task marked as complete with ID: {args.id}")
            print(f"Task with ID {args.id} marked as complete!")
            task = task_service.get_task_by_id(args.id)
            if task:
                display_task(task)
        else:
            logger.warning(f"Task with ID {args.id} not found")
            print(f"Error: Task with ID {args.id} not found", file=sys.stderr)
            sys.exit(1)
    elif args.command == 'incomplete':
        logger.info(f"Marking task as incomplete with ID: {args.id}")
        # Validate task ID
        if not args.id or not args.id.strip():
            logger.error("Invalid task ID provided")
            print("Error: Task ID cannot be empty", file=sys.stderr)
            sys.exit(1)

        # Mark task as incomplete
        if task_service.mark_incomplete(args.id):
            logger.info(f"Task marked as incomplete with ID: {args.id}")
            print(f"Task with ID {args.id} marked as incomplete!")
            task = task_service.get_task_by_id(args.id)
            if task:
                display_task(task)
        else:
            logger.warning(f"Task with ID {args.id} not found")
            print(f"Error: Task with ID {args.id} not found", file=sys.stderr)
            sys.exit(1)
    elif args.command is None:
        logger.debug("Showing help message")
        parser.print_help()
    else:
        logger.error(f"Unknown command: {args.command}")
        print(f"Unknown command: {args.command}", file=sys.stderr)
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()