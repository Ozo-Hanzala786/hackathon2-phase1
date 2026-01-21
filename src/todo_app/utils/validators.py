"""
Input validation utilities for the Console Todo Application
"""


def validate_task_title(title: str) -> bool:
    """
    Validate that a task title is not empty or whitespace-only.

    Args:
        title: The title to validate

    Returns:
        True if the title is valid, False otherwise
    """
    if not title:
        return False
    if not title.strip():
        return False
    return True


def validate_task_id(task_id: str) -> bool:
    """
    Validate that a task ID is not empty or whitespace-only.

    Args:
        task_id: The ID to validate

    Returns:
        True if the ID is valid, False otherwise
    """
    if not task_id:
        return False
    if not task_id.strip():
        return False
    return True


def validate_description(description: str) -> bool:
    """
    Validate that a description is not None (but can be empty).

    Args:
        description: The description to validate

    Returns:
        True if the description is valid, False otherwise
    """
    if description is None:
        return False
    return True


def sanitize_input(input_str: str) -> str:
    """
    Sanitize input string by stripping leading/trailing whitespace.

    Args:
        input_str: The input string to sanitize

    Returns:
        The sanitized string
    """
    if input_str is None:
        return ""
    return input_str.strip()


def is_valid_uuid(uuid_string: str) -> bool:
    """
    Check if a string is a valid UUID.

    Args:
        uuid_string: The string to validate

    Returns:
        True if the string is a valid UUID, False otherwise
    """
    import re
    uuid_regex = r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'
    return bool(re.match(uuid_regex, uuid_string))