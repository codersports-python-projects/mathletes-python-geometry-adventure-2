# Mathletes: Python Geometry Adventure 2 - explore_phase_solution_utils.py

# This module contains utility functions for the explore phase of the Mathletes Adventure.
# These functions help manage user profiles and validate inputs, supporting the main game logic.

import json
import os

# Constants
MIN_AGE = 10  # Minimum age allowed for players
MAX_AGE = 14  # Maximum age allowed for players
USER_DATA_FILE = 'user_data.json'  # File to store user profiles


def validate_age(age):
    """
    Validate the user's age.

    Parameters:
    age (str): The age input provided by the user.

    Returns:
    bool: True if age is a valid integer within the allowed range, False otherwise.
    """
    try:
        # Convert the age to an integer
        age_int = int(age)
        # Check if the age is within the allowed range
        return MIN_AGE <= age_int <= MAX_AGE
    except ValueError:
        # If conversion fails, the input is not a valid integer
        return False


def save_user_profile(user_profile):
    """
    Save the user's profile to a JSON file.

    Parameters:
    user_profile (dict): The user's profile containing name, age, and progress.
    """
    try:
        # Check if the user data file already exists
        if os.path.exists(USER_DATA_FILE):
            # Open the file and load existing data
            with open(USER_DATA_FILE, 'r') as file:
                data = json.load(file)
        else:
            # If file does not exist, start with an empty dictionary
            data = {}

        # Update the data with the new user profile
        data[user_profile['name']] = user_profile

        # Write the updated data back to the file
        with open(USER_DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
        print("User profile saved successfully.")
    except IOError as e:
        # Handle any I/O errors that occur during file operations
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
        # Check if the user data file exists
        if os.path.exists(USER_DATA_FILE):
            # Open the file and load the data
            with open(USER_DATA_FILE, 'r') as file:
                data = json.load(file)
                # Return the profile for the specified user name
                return data.get(user_name)
        else:
            # If the file does not exist, inform the user
            print("No user data file found.")
            return None
    except IOError as e:
        # Handle any I/O errors that occur during file operations
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
    # Extract user details from the profile
    name = user_profile.get('name', 'Unknown')
    age = user_profile.get('age', 'Unknown')
    progress = user_profile.get('progress', [])
    # Convert progress list to a string
    progress_str = ', '.join(progress) if progress else 'No progress yet'
    # Return the formatted string
    return f"Name: {name}\nAge: {age}\nProgress: {progress_str}"
