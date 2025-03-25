# Mathletes: Python Geometry Adventure 2 - explore_phase_skeleton_utils.py

# Utility functions and shared utilities for the Mathletes Adventure application.

import json
import os

# Constants
MIN_AGE = 10
MAX_AGE = 14
USER_DATA_FILE = 'user_data.json'


def validate_age(age):
    """
    Validate the user's age.

    Parameters:
    age (str): The age input provided by the user.

    Returns:
    bool: True if age is a valid integer within the allowed range, False otherwise.
    """
    # TODO: Implement the logic to validate the user's age
    # Hint: Use try-except to handle conversion and check if age is within range
    pass


def save_user_profile(user_profile):
    """
    Save the user's profile to a JSON file.

    Parameters:
    user_profile (dict): The user's profile containing name, age, and progress.
    """
    # TODO: Implement the logic to save the user's profile
    # Hint: Use json module to write to a file, handle exceptions for file operations
    pass


def load_user_profile(user_name):
    """
    Load a user's profile from a JSON file.

    Parameters:
    user_name (str): The name of the user whose profile is to be loaded.

    Returns:
    dict: The user's profile if found, None otherwise.
    """
    # TODO: Implement the logic to load a user's profile
    # Hint: Check if the file exists, read the file, and handle exceptions
    pass


def format_user_profile(user_profile):
    """
    Format the user's profile for display.

    Parameters:
    user_profile (dict): The user's profile containing name, age, and progress.

    Returns:
    str: A formatted string representation of the user's profile.
    """
    # TODO: Implement the logic to format the user's profile
    # Hint: Use string formatting to create a readable output
    pass

# Note to students: Complete each function by following the hints provided in the comments.
# Remember to test your functions to ensure they work as expected!