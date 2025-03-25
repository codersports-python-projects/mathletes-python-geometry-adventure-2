# Mathletes: Python Geometry Adventure 2 - launch_phase_student_skeleton_utils.py

# This module provides utility functions for the Mathletes Adventure application.
# Students will implement and enhance these functions as part of their learning journey.

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
        # TODO: Check if the user data file exists and load existing data
        # If the file does not exist, initialize an empty dictionary
        
        # TODO: Update the data with the new user profile

        # TODO: Save the updated data back to the JSON file
        
        print("User profile saved successfully.")
    except IOError as e:
        # TODO: Implement error handling for file operations
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
        # TODO: Implement logic to check if the user data file exists
        # If it exists, load the data and return the profile for the given user name

        # TODO: Handle the case where the file does not exist
        
    except IOError as e:
        # TODO: Implement error handling for file operations
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
    # TODO: Extract user details from the profile dictionary
    # Format the details into a readable string
    
    return ""  # TODO: Return the formatted string

# Additional utility functions can be added below as needed
# Students are encouraged to think creatively and expand the functionality of this module
