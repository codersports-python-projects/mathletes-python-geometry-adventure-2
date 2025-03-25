# Mathletes: Python Geometry Adventure 2 - explore_phase_skeleton_features.py

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Features Module Skeleton
# This module is designed to provide interactive features to enhance the user experience.
# Students will implement functions to provide hints, interactive guides, and visualizations.


def provide_hint(challenge_name):
    """
    Provide hints for the given challenge.

    Parameters:
    challenge_name (str): The name of the challenge for which a hint is requested.

    Returns:
    str: A hint message relevant to the challenge.
    """
    # TODO: Add more challenges and their corresponding hints
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
    # TODO: Implement interactive guides for more challenges
    if challenge_name == "Calculate Area":
        print("Let's calculate the area of a triangle.")
        # Pseudocode:
        # 1. Prompt user for base and height of the triangle
        # 2. Calculate area using the formula
        # 3. Display the calculated area
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area}.")
    elif challenge_name == "Estimate Volume":
        print("Let's estimate the volume of a cylinder.")
        # Pseudocode:
        # 1. Prompt user for radius and height of the cylinder
        # 2. Calculate volume using the formula
        # 3. Display the calculated volume
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
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
    # TODO: Add visualization for more challenges
    if challenge_name == "Calculate Area":
        # Pseudocode:
        # 1. Extract base and height from data
        # 2. Plot the triangle using Matplotlib
        base = data.get('base', 0)
        height = data.get('height', 0)
        plt.figure()
        plt.plot([0, base, base, 0, 0], [0, 0, height, height, 0], 'b-')
        plt.fill_between([0, base], 0, height, color='skyblue', alpha=0.5)
        plt.title('Triangle Area')
        plt.xlabel('Base')
        plt.ylabel('Height')
        plt.show()
    elif challenge_name == "Estimate Volume":
        # Pseudocode:
        # 1. Extract radius and height from data
        # 2. Plot the cylinder using Matplotlib
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
        plt.show()
    else:
        print("Visualization not available for this challenge.")

# Note to students: Use this skeleton as a starting point for implementing interactive features.
# Follow the pseudocode and comments to complete the functions and add new features.