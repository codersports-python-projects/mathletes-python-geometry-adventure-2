# Mathletes: Python Geometry Adventure 2 - launch_phase_student_test_project.py

# Import the unittest module for creating test cases
import unittest

# Import the main components of the project to be tested
from main import MathletesAdventure
import utils

class TestMathletesAdventure(unittest.TestCase):
    """
    Test suite for Mathletes: Python Geometry Adventure 2
    This class contains test cases to validate the functionality of the MathletesAdventure class.
    """

    def setUp(self):
        """
        Set up test fixtures. This method is called before each test.
        """
        self.adventure = MathletesAdventure()

    def test_welcome_message_display(self):
        """
        Test Case 1: Welcome Message Display
        Objective: Verify that the welcome message and instructions are displayed correctly.
        """
        # TODO: Implement a method to capture printed output and verify the welcome message
        pass

    def test_user_input_validation(self):
        """
        Test Case 2: User Input Validation
        Objective: Ensure that user input for age is validated correctly.
        """
        # Test with invalid age
        self.assertFalse(utils.validate_age("abc"))  # Non-numeric input
        self.assertFalse(utils.validate_age("9"))    # Below minimum age
        # Test with valid age
        self.assertTrue(utils.validate_age("12"))   # Valid age

    def test_area_calculation(self):
        """
        Test Case 3: Area Calculation
        Objective: Test functions for calculating areas of various shapes.
        """
        # TODO: Implement test for area calculation function
        pass

    def test_perimeter_calculation(self):
        """
        Test Case 4: Perimeter Calculation
        Objective: Test functions for calculating perimeters of various shapes.
        """
        # TODO: Implement test for perimeter calculation function
        pass

    def test_plotting_graphs(self):
        """
        Test Case 5: Plotting Graphs
        Objective: Ensure plots are correctly labeled and scaled using Matplotlib.
        """
        # TODO: Implement test for plotting graphs
        pass

    # Additional test cases can be added here following the same pattern

if __name__ == '__main__':
    unittest.main()
