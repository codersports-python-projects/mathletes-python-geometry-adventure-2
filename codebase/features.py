# Mathletes: Python Geometry Adventure 2 - features.py

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

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
    if challenge_name == "Calculate Area":
        print("Let's calculate the area of a triangle.")
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area}.")
    elif challenge_name == "Estimate Volume":
        print("Let's estimate the volume of a cylinder.")
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
    if challenge_name == "Calculate Area":
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
