# Mathletes: Python Geometry Adventure 2 - utils.py

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
    try:
        age_int = int(age)
        return MIN_AGE <= age_int <= MAX_AGE
    except ValueError:
        return False


def save_user_profile(user_profile):
    """
    Save the user's profile to a JSON file.

    Parameters:
    user_profile (dict): The user's profile containing name, age, and progress.
    """
    try:
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r') as file:
                data = json.load(file)
        else:
            data = {}

        data[user_profile['name']] = user_profile

        with open(USER_DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
        print("User profile saved successfully.")
    except IOError as e:
        print(f"Error saving user profile: {e}")


def load_user_profile(user_name):
    """
    Load a user's profile from a JSON file.

    Parameters:
    user_name (str): The name of the user whose profile is to be loaded.

    Returns:
    dict: The user's profile if found, None otherwise.
    """
    try:
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r') as file:
                data = json.load(file)
                return data.get(user_name)
        else:
            print("No user data file found.")
            return None
    except IOError as e:
        print(f"Error loading user profile: {e}")
        return None


def format_user_profile(user_profile):
    """
    Format the user's profile for display.

    Parameters:
    user_profile (dict): The user's profile containing name, age, and progress.

    Returns:
    str: A formatted string representation of the user's profile.
    """
    name = user_profile.get('name', 'Unknown')
    age = user_profile.get('age', 'Unknown')
    progress = user_profile.get('progress', [])
    progress_str = ', '.join(progress) if progress else 'No progress yet'
    return f"Name: {name}\nAge: {age}\nProgress: {progress_str}"
