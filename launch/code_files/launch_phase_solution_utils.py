# Mathletes: Python Geometry Adventure 2 - launch_phase_solution_utils.py

import json
import os
import logging

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='mathletes_debug.log',
                    filemode='w')

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
        if MIN_AGE <= age_int <= MAX_AGE:
            logging.debug(f"Validated age: {age_int}")
            return True
        else:
            logging.warning(f"Age {age_int} is out of valid range.")
            return False
    except ValueError:
        logging.error(f"Invalid age input: {age}")
        return False


def save_user_profile(user_profile):
    """
    Save the user's profile to a JSON file.

    Parameters:
    user_profile (dict): The user's profile containing name, age, and progress.
    """
    try:
        data = {}
        if os.path.exists(USER_DATA_FILE):
            with open(USER_DATA_FILE, 'r') as file:
                data = json.load(file)
                logging.debug("Loaded existing user data.")

        data[user_profile['name']] = user_profile

        with open(USER_DATA_FILE, 'w') as file:
            json.dump(data, file, indent=4)
            logging.info(f"User profile for {user_profile['name']} saved successfully.")
    except IOError as e:
        logging.error(f"Error saving user profile: {e}")


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
                logging.debug("User data file loaded for profile retrieval.")
                user_profile = data.get(user_name)
                if user_profile:
                    logging.info(f"User profile for {user_name} loaded successfully.")
                else:
                    logging.warning(f"User profile for {user_name} not found.")
                return user_profile
        else:
            logging.warning("No user data file found.")
            return None
    except IOError as e:
        logging.error(f"Error loading user profile: {e}")
        return None


def format_user_profile(user_profile):
    """
    Format the user's profile for display.

    Parameters:
    user_profile (dict): The user's profile containing name, age, and progress.

    Returns:
    str: A formatted string representation of the user's profile.
    """
    try:
        name = user_profile.get('name', 'Unknown')
        age = user_profile.get('age', 'Unknown')
        progress = user_profile.get('progress', [])
        progress_str = ', '.join(progress) if progress else 'No progress yet'
        formatted_profile = f"Name: {name}\nAge: {age}\nProgress: {progress_str}"
        logging.debug(f"Formatted user profile: {formatted_profile}")
        return formatted_profile
    except Exception as e:
        logging.error(f"Error formatting user profile: {e}")
        return "Error formatting profile."