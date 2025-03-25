# Mathletes: Python Geometry Adventure 2 - build_phase_skeleton_main.py

# Import necessary modules
import utils
import features
from challenge_modules import geometry_challenges

# Main Controller Class
class MathletesAdventure:
    def __init__(self):
        """
        Initialize the game environment and global variables.
        This is where we set up the initial state of our game, like user profile and available challenges.
        """
        self.user_profile = {}  # To store user details and progress
        self.challenges = ["Calculate Area", "Estimate Volume"]  # List of challenges
        self.current_challenge = None  # To track the current challenge

    def start_adventure(self):
        """
        Start the adventure by displaying a welcome message and instructions.
        This method kicks off the game and guides the user to set up their profile.
        """
        print("Welcome to Mathletes: Python Geometry Adventure 2! 🚀")
        print("Embark on a Python-powered journey through the world of geometry and mathematics!")
        self.user_setup()  # Proceed to user setup

    def user_setup(self):
        """
        Prompt user for name and age, validate input, and store user profile.
        This method ensures the user is of the appropriate age and stores their basic info.
        """
        while True:
            user_name = input("Enter your name: ")  # Get user's name
            user_age = input("Enter your age: ")  # Get user's age
            # Validate age using a utility function
            if utils.validate_age(user_age):
                self.user_profile = {'name': user_name, 'age': int(user_age), 'progress': []}  # Store profile
                break  # Exit loop if age is valid
            else:
                print("Invalid age. Please enter a number between 10 and 14.")
        self.select_challenge()  # Proceed to challenge selection

    def select_challenge(self):
        """
        Present a list of challenges and allow user to select one.
        This method lets the user choose which mathematical challenge they want to tackle.
        """
        print("Select a challenge:")
        for index, challenge in enumerate(self.challenges, start=1):
            print(f"{index}. {challenge}")  # Display challenges with numbers
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))  # Get user's choice
                if 1 <= choice <= len(self.challenges):
                    self.current_challenge = self.challenges[choice - 1]  # Set current challenge
                    break  # Exit loop if choice is valid
                else:
                    print("Invalid choice. Please select a valid challenge number.")
            except ValueError:
                print("Please enter a valid number.")
        self.load_challenge_module()  # Load the selected challenge

    def load_challenge_module(self):
        """
        Load the relevant module for the selected challenge.
        This method connects the selected challenge to its corresponding module.
        """
        if self.current_challenge == "Calculate Area":
            # TODO: Implement the calculate_area function in geometry_challenges
            geometry_challenges.calculate_area(self.user_profile)
        elif self.current_challenge == "Estimate Volume":
            # TODO: Implement the estimate_volume function in geometry_challenges
            geometry_challenges.estimate_volume(self.user_profile)
        self.evaluate_solution()  # Proceed to solution evaluation

    def evaluate_solution(self):
        """
        Evaluate the user's solution and provide feedback.
        This method checks the user's solution and gives feedback.
        """
        # TODO: Implement evaluation logic
        print("Evaluating solution...")
        print("Solution evaluated. Great job!")
        self.repeat_or_end_adventure()  # Ask user if they want to continue

    def repeat_or_end_adventure(self):
        """
        Offer the option to try another challenge or exit.
        This method lets the user decide to play another round or finish the game.
        """
        choice = input("Would you like to try another challenge? (yes/no): ").strip().lower()
        if choice == 'yes':
            self.select_challenge()  # Restart challenge selection
        else:
            self.save_progress()  # Save progress before exiting
            print("Thank you for playing Mathletes: Python Geometry Adventure 2! Goodbye!")

    def save_progress(self):
        """
        Save the user's progress to a file.
        This method ensures that the user's progress is saved for future sessions.
        """
        # TODO: Implement save_user_profile function in utils
        utils.save_user_profile(self.user_profile)

# Main execution
if __name__ == "__main__":
    adventure = MathletesAdventure()  # Create an instance of the game
    adventure.start_adventure()  # Start the adventure