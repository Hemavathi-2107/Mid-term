
"""
This module contains test cases for various commands in the application, including
add, subtract, multiply, divide, and menu commands. Each command is tested with
valid and invalid inputs to ensure expected behavior. The tests also include scenarios
for edge cases such as division by zero and invalid arguments.
"""
import logging
from unittest.mock import Mock, patch
import pytest
from app.plugins.addcommand import Add
from app.plugins.subtractcommand import Subtract
from app.plugins.multiplycommand import Multiply
from app.plugins.dividecommand import Divide
from app.plugins.menucommand import Menu

# Configure logging for tests
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@pytest.fixture
def mock_command_handler():
    '''Mock command handler'''
    mock_handler = Mock()
    mock_handler.Register_Command = Mock()
    mock_handler.Execute_Command = Mock()
    logger.debug("Mock command handler created.")
    return mock_handler

@pytest.fixture
def add_command(mock_command_handler):
    '''Fixture for Add command'''
    logger.debug("Creating Add command fixture.")
    return Add(command_handler=mock_command_handler)

@pytest.fixture
def subtract_command(mock_command_handler):
    '''Fixture for Subtract command'''
    logger.debug("Creating Subtract command fixture.")
    return Subtract(command_handler=mock_command_handler)

@pytest.fixture
def multiply_command(mock_command_handler):
    '''Fixture for Multiply command'''
    logger.debug("Creating Multiply command fixture.")
    return Multiply(command_handler=mock_command_handler)

@pytest.fixture
def divide_command(mock_command_handler):
    '''Fixture for Divide command'''
    logger.debug("Creating Divide command fixture.")
    return Divide(command_handler=mock_command_handler)

@pytest.fixture
def menu_command(mock_command_handler):
    '''Fixture for Menu Command'''
    # Mock command handler to return the list of commands
    mock_command_handler.Get_Registered_Commands = Mock(return_value=["Add", "Subtract", "Multiply", "Divide", "Menu"])
    logger.debug("Creating Menu command fixture.")
    return Menu(command_handler=mock_command_handler)


# Testing the Add Command
class TestAddCommand:
    '''Test the Add command'''

    def test_add(self, add_command, capsys):
        '''Test successful addition'''
        logger.debug("Running test for successful addition with Add command.")
        add_command.execute('2', '3')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "2 + 3 = 5" in captured.out

    def test_add_one_argument(self, add_command, capsys):
        '''Test when only one argument is given'''
        logger.debug("Running test for Add command with one argument.")
        add_command.execute('2')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "Only two arguments must be given" in captured.out

    def test_add_invalid_args(self, add_command, capsys):
        '''Test invalid arguments'''
        logger.debug("Running test for Add command with invalid arguments.")
        add_command.execute('x', '2')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_add_error(self, add_command, capsys):
        '''Test when the calculator throws an error'''
        logger.debug("Running test for Add command error scenario.")
        with patch('app.plugins.addcommand.Calculator.add', side_effect=ValueError("Error")):
            add_command.execute('4', '2')
            captured = capsys.readouterr()
            logger.debug("Captured output: %s", captured.out)
            assert "Error" in captured.out


# Testing the Subtract Command
class TestSubtractCommand:
    '''Test the Subtract command'''

    def test_subtract(self, subtract_command, capsys):
        '''Test successful subtraction'''
        logger.debug("Running test for successful subtraction with Subtract command.")
        subtract_command.execute('4', '2')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "4 - 2 = 2" in captured.out

    def test_subtract_one_argument(self, subtract_command, capsys):
        '''Test when only one argument is given'''
        logger.debug("Running test for Subtract command with one argument.")
        subtract_command.execute('4')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "Only two arguments must be given" in captured.out

    def test_subtract_invalid_args(self, subtract_command, capsys):
        '''Test invalid arguments'''
        logger.debug("Running test for Subtract command with invalid arguments.")
        subtract_command.execute('x', '3')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_subtract_negative_numbers(self, subtract_command, capsys):
        '''Test subtraction with negative numbers'''
        logger.debug("Running test for Subtract command with negative numbers.")
        subtract_command.execute('-5', '3')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "-5 - 3 = -8" in captured.out

    def test_subtract_error(self, subtract_command, capsys):
        '''Test when the calculator throws an error'''
        logger.debug("Running test for Subtract command error scenario.")
        with patch('app.plugins.subtractcommand.Calculator.subtract', side_effect=ValueError("Error")):
            subtract_command.execute('4', '2')
            captured = capsys.readouterr()
            logger.debug("Captured output: %s", captured.out)
            assert "Error" in captured.out


# Testing the Multiply Command
class TestMultiplyCommand:
    '''Test the Multiply command'''

    def test_multiply(self, multiply_command, capsys):
        '''Test successful multiplication'''
        logger.debug("Running test for successful multiplication with Multiply command.")
        multiply_command.execute('4', '2')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "4 * 2 = 8" in captured.out

    def test_multiply_one_argument(self, multiply_command, capsys):
        '''Test when only one argument is given'''
        logger.debug("Running test for Multiply command with one argument.")
        multiply_command.execute('4')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "Only two arguments must be given" in captured.out

    def test_multiply_invalid_args(self, multiply_command, capsys):
        '''Test invalid arguments'''
        logger.debug("Running test for Multiply command with invalid arguments.")
        multiply_command.execute('x', '3')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_multiply_error(self, multiply_command, capsys):
        '''Test when the calculator throws an error'''
        logger.debug("Running test for Multiply command error scenario.")
        with patch('app.plugins.multiplycommand.Calculator.multiply', side_effect=ValueError("Error")):
            multiply_command.execute('4', '2')
            captured = capsys.readouterr()
            logger.debug("Captured output: %s", captured.out)
            assert "Error" in captured.out


# Testing the Divide Command
class TestDivideCommand:
    '''Test the Divide command'''

    def test_divide(self, divide_command, capsys):
        '''Test successful division'''
        logger.debug("Running test for successful division with Divide command.")
        divide_command.execute('4', '2')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "4 / 2 = 2" in captured.out

    def test_divide_one_argument(self, divide_command, capsys):
        '''Test when only one argument is given'''
        logger.debug("Running test for Divide command with one argument.")
        divide_command.execute('4')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "Only two arguments must be given" in captured.out

    def test_divide_invalid_args(self, divide_command, capsys):
        '''Test invalid arguments'''
        logger.debug("Running test for Divide command with invalid arguments.")
        divide_command.execute('x', '3')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "One of the entered numbers is invalid. Please enter valid inputs." in captured.out

    def test_divide_by_zero(self, divide_command, capsys):
        '''Test division by zero'''
        logger.debug("Running test for Divide command with division by zero.")
        divide_command.execute('9', '0')
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "Error: Cannot divide by zero" in captured.out

    def test_divide_error(self, divide_command, capsys):
        '''Test when the calculator throws an error'''
        logger.debug("Running test for Divide command error scenario.")
        with patch('app.plugins.dividecommand.Calculator.divide', side_effect=ValueError("Error")):
            divide_command.execute('4', '2')
            captured = capsys.readouterr()
            logger.debug("Captured output: %s", captured.out)
            assert "Error" in captured.out


# Testing the Menu Command
class TestMenuCommand:
    '''Test the Menu command'''

    def test_menu_command(self, menu_command, capsys):
        '''Test that the Menu command displays the list of available commands'''
        logger.debug("Running test for Menu command.")
        menu_command.execute()
        captured = capsys.readouterr()
        logger.debug("Captured output: %s", captured.out)
        assert "Commands Available:" in captured.out, "MenuCommand should display the available commands"
        assert "Add" in captured.out
        assert "Subtract" in captured.out
        assert "Multiply" in captured.out
        assert "Divide" in captured.out
        assert "Menu" in captured.out
