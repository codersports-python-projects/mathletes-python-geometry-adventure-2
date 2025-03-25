# Mathletes: Python Geometry Adventure 2 - launch_phase_solution_features.py

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import logging

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Features Module
# This module implements additional interactive features to enhance the user experience.


def provide_hint(challenge_name):
    """
    Provide hints for the given challenge.

    Parameters:
    challenge_name (str): The name of the challenge for which a hint is requested.

    Returns:
    str: A hint message relevant to the challenge.
    """
    logging.debug(f"Providing hint for challenge: {challenge_name}")
    hints = {
        "Calculate Area": "Remember the formula for the area of a triangle is 0.5 * base * height.",
        "Estimate Volume": "For a cylinder, volume is π * radius^2 * height."
    }
    return hints.get(challenge_name, "No hints available for this challenge.")


def interactive_guide(challenge_name):
    """
    Provide an interactive guide for solving the challenge.

    Parameters:
    challenge_name (str): The name of the challenge for which guidance is requested.

    Returns:
    None
    """
    logging.debug(f"Starting interactive guide for challenge: {challenge_name}")
    if challenge_name == "Calculate Area":
        print("Let's calculate the area of a triangle.")
        base = get_positive_float("Enter the base of the triangle: ")
        height = get_positive_float("Enter the height of the triangle: ")
        area = 0.5 * base * height
        print(f"The area of the triangle is {area}.")
    elif challenge_name == "Estimate Volume":
        print("Let's estimate the volume of a cylinder.")
        radius = get_positive_float("Enter the radius of the cylinder: ")
        height = get_positive_float("Enter the height of the cylinder: ")
        volume = np.pi * radius**2 * height
        print(f"The volume of the cylinder is {volume}.")
    else:
        print("Interactive guide not available for this challenge.")


def visualize_solution(challenge_name, data):
    """
    Visualize the solution for the given challenge using Matplotlib.

    Parameters:
    challenge_name (str): The name of the challenge to visualize.
    data (dict): The data required for visualization.

    Returns:
    None
    """
    logging.debug(f"Visualizing solution for challenge: {challenge_name} with data: {data}")
    if challenge_name == "Calculate Area":
        base = data.get('base', 0)
        height = data.get('height', 0)
        plt.figure()
        plt.plot([0, base, base, 0, 0], [0, 0, height, height, 0], 'b-')
        plt.fill_between([0, base], 0, height, color='skyblue', alpha=0.5)
        plt.title('Triangle Area')
        plt.xlabel('Base')
        plt.ylabel('Height')
        plt.grid(True)
        plt.show()
    elif challenge_name == "Estimate Volume":
        radius = data.get('radius', 0)
        height = data.get('height', 0)
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        x = np.linspace(-radius, radius, 100)
        z = np.linspace(0, height, 100)
        X, Z = np.meshgrid(x, z)
        Y = np.sqrt(radius**2 - X**2)
        ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100)
        ax.plot_surface(X, -Y, Z, alpha=0.5, rstride=100, cstride=100)
        ax.set_title('Cylinder Volume')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    else:
        print("Visualization not available for this challenge.")


def get_positive_float(prompt):
    """
    Prompt the user for a positive float value.

    Parameters:
    prompt (str): The input prompt for the user.

    Returns:
    float: The validated positive float input by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Example of how these functions might be used in the main application
if __name__ == "__main__":
    # Example usage of the interactive guide
    interactive_guide("Calculate Area")

    # Example data for visualization
    example_data = {'base': 5, 'height': 10}
    visualize_solution("Calculate Area", example_data)

    # Example hint
    print(provide_hint("Calculate Area"))
