# Mathletes: Python Geometry Adventure 2 - explore_phase_solution_main.py

# Import necessary modules
import utils  # Utility functions for validation and data handling
import features  # Additional features like hints and visualizations
from challenge_modules import geometry_challenges  # Challenge-specific functions

# Main Controller Class
class MathletesAdventure:
    def __init__(self):
        """
        Initialize the game environment and global variables.
        This is where we set up everything we need to start the adventure.
        """
        self.user_profile = {}  # Dictionary to store user information
        self.challenges = ["Calculate Area", "Estimate Volume"]  # List of available challenges
        self.current_challenge = None  # Variable to keep track of the current challenge

    def start_adventure(self):
        """
        Start the adventure by displaying a welcome message and instructions.
        This function kicks off the entire game.
        """
        print("Welcome to Mathletes: Python Geometry Adventure 2! 🚀")
        print("Embark on a Python-powered journey through the world of geometry and mathematics!")
        self.user_setup()  # Move to the next step: setting up user information

    def user_setup(self):
        """
        Prompt user for name and age, validate input, and store user profile.
        This ensures we have all the necessary information to personalize the game.
        """
        while True:
            user_name = input("Enter your name: ")  # Get the user's name
            user_age = input("Enter your age: ")  # Get the user's age
            # Validate the age input
            if utils.validate_age(user_age):
                # Store the user's profile in a dictionary
                self.user_profile = {'name': user_name, 'age': int(user_age), 'progress': []}
                break  # Exit the loop if age is valid
            else:
                print("Invalid age. Please enter a number between 10 and 14.")
        self.select_challenge()  # Proceed to challenge selection

    def select_challenge(self):
        """
        Present a list of challenges and allow the user to select one.
        This function lets the user choose what they want to work on.
        """
        print("Select a challenge:")
        # Display each challenge with a number
        for index, challenge in enumerate(self.challenges, start=1):
            print(f"{index}. {challenge}")
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))  # User selects a challenge
                # Check if the choice is valid
                if 1 <= choice <= len(self.challenges):
                    self.current_challenge = self.challenges[choice - 1]  # Set the current challenge
                    break  # Exit the loop if choice is valid
                else:
                    print("Invalid choice. Please select a valid challenge number.")
            except ValueError:
                print("Please enter a valid number.")
        self.load_challenge_module()  # Load the selected challenge

    def load_challenge_module(self):
        """
        Load the relevant module for the selected challenge.
        This function directs the program to the appropriate challenge logic.
        """
        if self.current_challenge == "Calculate Area":
            geometry_challenges.calculate_area(self.user_profile)  # Call the area calculation function
        elif self.current_challenge == "Estimate Volume":
            geometry_challenges.estimate_volume(self.user_profile)  # Call the volume estimation function
        self.evaluate_solution()  # Move to solution evaluation

    def evaluate_solution(self):
        """
        Evaluate the user's solution and provide feedback.
        Here, we check if the user's solution is correct and give feedback.
        """
        print("Evaluating solution...")  # Placeholder for evaluation logic
        print("Solution evaluated. Great job!")  # Feedback to the user
        self.repeat_or_end_adventure()  # Ask if the user wants to continue

    def repeat_or_end_adventure(self):
        """
        Offer the option to try another challenge or exit.
        This function lets the user decide if they want to keep playing or finish.
        """
        choice = input("Would you like to try another challenge? (yes/no): ").strip().lower()
        if choice == 'yes':
            self.select_challenge()  # Go back to challenge selection
        else:
            self.save_progress()  # Save the user's progress
            print("Thank you for playing Mathletes: Python Geometry Adventure 2! Goodbye!")

    def save_progress(self):
        """
        Save the user's progress to a file.
        This ensures that the user's progress is not lost and can be resumed later.
        """
        utils.save_user_profile(self.user_profile)  # Call utility function to save data

# Main execution
if __name__ == "__main__":
    adventure = MathletesAdventure()  # Create an instance of the game
    adventure.start_adventure()  # Start the game