# Mathletes: Python Geometry Adventure 2 - explore_phase_skeleton_main.py

# Import necessary modules
import utils
import features
from challenge_modules import geometry_challenges

# Main Controller Class
class MathletesAdventure:
    def __init__(self):
        """Initialize the game environment and global variables."""
        self.user_profile = {}
        self.challenges = ["Calculate Area", "Estimate Volume"]
        self.current_challenge = None

    def start_adventure(self):
        """Start the adventure by displaying welcome message and instructions."""
        # TODO: Display a welcome message and instructions for the game
        print("Welcome to Mathletes: Python Geometry Adventure 2! 🚀")
        print("Embark on a Python-powered journey through the world of geometry and mathematics!")
        self.user_setup()

    def user_setup(self):
        """Prompt user for name and age, validate input, and store user profile."""
        # TODO: Implement user input for name and age with validation
        while True:
            user_name = input("Enter your name: ")
            user_age = input("Enter your age: ")
            if utils.validate_age(user_age):
                self.user_profile = {'name': user_name, 'age': int(user_age), 'progress': []}
                break
            else:
                print("Invalid age. Please enter a number between 10 and 14.")
        self.select_challenge()

    def select_challenge(self):
        """Present a list of challenges and allow user to select one."""
        # TODO: Display list of challenges and get user choice
        print("Select a challenge:")
        for index, challenge in enumerate(self.challenges, start=1):
            print(f"{index}. {challenge}")
        while True:
            try:
                choice = int(input("Enter the number of your choice: "))
                if 1 <= choice <= len(self.challenges):
                    self.current_challenge = self.challenges[choice - 1]
                    break
                else:
                    print("Invalid choice. Please select a valid challenge number.")
            except ValueError:
                print("Please enter a valid number.")
        self.load_challenge_module()

    def load_challenge_module(self):
        """Load the relevant module for the selected challenge."""
        # TODO: Load and execute the selected challenge module
        if self.current_challenge == "Calculate Area":
            geometry_challenges.calculate_area(self.user_profile)
        elif self.current_challenge == "Estimate Volume":
            geometry_challenges.estimate_volume(self.user_profile)
        self.evaluate_solution()

    def evaluate_solution(self):
        """Evaluate the user's solution and provide feedback."""
        # TODO: Implement solution evaluation logic
        print("Evaluating solution...")
        print("Solution evaluated. Great job!")
        self.repeat_or_end_adventure()

    def repeat_or_end_adventure(self):
        """Offer the option to try another challenge or exit."""
        # TODO: Provide options to repeat or end the adventure
        choice = input("Would you like to try another challenge? (yes/no): ").strip().lower()
        if choice == 'yes':
            self.select_challenge()
        else:
            self.save_progress()
            print("Thank you for playing Mathletes: Python Geometry Adventure 2! Goodbye!")

    def save_progress(self):
        """Save the user's progress to a file."""
        # TODO: Implement saving user profile to a file
        utils.save_user_profile(self.user_profile)

# Main execution
if __name__ == "__main__":
    adventure = MathletesAdventure()
    adventure.start_adventure()