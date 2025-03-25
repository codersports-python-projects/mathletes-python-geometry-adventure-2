import unittest
from unittest.mock import patch, mock_open
import json
import os
import utils
import features
from main import MathletesAdventure

class TestMathletesAdventure(unittest.TestCase):
    def setUp(self):
        """Set up the environment for each test."""
        self.adventure = MathletesAdventure()

    @patch('builtins.input', side_effect=['TestUser', '12'])
    def test_user_setup_valid_age(self, mock_input):
        """Test user setup with valid age input."""
        self.adventure.user_setup()
        self.assertEqual(self.adventure.user_profile['name'], 'TestUser')
        self.assertEqual(self.adventure.user_profile['age'], 12)

    @patch('builtins.input', side_effect=['TestUser', '9', '12'])
    def test_user_setup_invalid_age(self, mock_input):
        """Test user setup with invalid age input followed by valid input."""
        self.adventure.user_setup()
        self.assertEqual(self.adventure.user_profile['age'], 12)

    @patch('builtins.input', side_effect=['1'])
    def test_select_challenge(self, mock_input):
        """Test selecting a challenge."""
        self.adventure.challenges = ["Calculate Area"]
        self.adventure.select_challenge()
        self.assertEqual(self.adventure.current_challenge, "Calculate Area")

    @patch('builtins.input', side_effect=['no'])
    def test_repeat_or_end_adventure(self, mock_input):
        """Test ending the adventure after one challenge."""
        with patch('utils.save_user_profile') as mock_save:
            self.adventure.repeat_or_end_adventure()
            mock_save.assert_called_once()

class TestUtils(unittest.TestCase):
    def test_validate_age_valid(self):
        """Test age validation with valid age."""
        self.assertTrue(utils.validate_age('12'))

    def test_validate_age_invalid(self):
        """Test age validation with invalid age."""
        self.assertFalse(utils.validate_age('abc'))
        self.assertFalse(utils.validate_age('9'))

    @patch('builtins.open', new_callable=mock_open, read_data='{}')
    def test_save_user_profile(self, mock_file):
        """Test saving user profile to a file."""
        user_profile = {'name': 'TestUser', 'age': 12, 'progress': []}
        utils.save_user_profile(user_profile)
        mock_file.assert_called_once_with(utils.USER_DATA_FILE, 'w')
        handle = mock_file()
        handle.write.assert_called_once_with(json.dumps({'TestUser': user_profile}, indent=4))

class TestFeatures(unittest.TestCase):
    @patch('builtins.input', side_effect=['5', '10'])
    def test_interactive_guide_calculate_area(self, mock_input):
        """Test interactive guide for calculating area of a triangle."""
        with patch('builtins.print') as mock_print:
            features.interactive_guide("Calculate Area")
            mock_print.assert_any_call("The area of the triangle is 25.0.")

    @patch('matplotlib.pyplot.show')
    def test_visualize_solution_calculate_area(self, mock_show):
        """Test visualization of solution for calculating area."""
        data = {'base': 5, 'height': 10}
        features.visualize_solution("Calculate Area", data)
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()