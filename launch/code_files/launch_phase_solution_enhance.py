# enhancements.py

import logging
import time
from functools import wraps

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("mathletes.log"),
                              logging.StreamHandler()])

# Decorator for timing functions to optimize performance
# This decorator logs the time taken by functions to execute

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.debug(f"{func.__name__} executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

# Enhanced error handling
# Custom exception classes for specific error scenarios

class InvalidInputError(Exception):
    """Exception raised for errors in the input."""
    def __init__(self, message="Invalid input provided"):
        self.message = message
        super().__init__(self.message)

class CalculationError(Exception):
    """Exception raised for errors in the calculation process."""
    def __init__(self, message="Error occurred during calculation"):
        self.message = message
        super().__init__(self.message)

# Example of a function with enhanced logging and error handling

@timing_decorator
def calculate_area(base, height):
    """
    Calculate the area of a triangle.

    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    try:
        if base <= 0 or height <= 0:
            raise InvalidInputError("Base and height must be positive numbers.")
        area = 0.5 * base * height
        logging.info(f"Calculated area: {area}")
        return area
    except InvalidInputError as e:
        logging.error(e)
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise CalculationError from e

# Example of a function to demonstrate usage of enhanced logging and error handling

def main():
    """Main function to demonstrate enhancements."""
    try:
        base = 5.0
        height = 10.0
        logging.info("Starting area calculation")
        area = calculate_area(base, height)
        logging.info(f"Area of the triangle is: {area}")
    except InvalidInputError as e:
        logging.error(f"Invalid input error: {e}")
    except CalculationError as e:
        logging.error(f"Calculation error: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
