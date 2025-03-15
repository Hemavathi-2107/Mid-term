"""
This module contains test cases for the CommandHandler class, which manages
the registration and execution of various commands like add, subtract, multiply,
and divide. Each test ensures that the commands are correctly registered and executed,
including handling edge cases such as division by zero and invalid commands.
"""
import unittest
import logging
from app.commands import CommandHandler
from app import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

# Configure the logger for testing
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TestCommandHandler(unittest.TestCase):
    """Test suite for CommandHandler."""

    def setUp(self):
        """Initialize CommandHandler and register commands before each test."""
        self.command_handler = CommandHandler()
        # Register commands with logging
        logger.info("Registering commands for testing...")
        self.command_handler.Register_Command("add", AddCommand())
        logger.info("Command 'add' registered.")
        self.command_handler.Register_Command("subtract", SubtractCommand())
        logger.info("Command 'subtract' registered.")
        self.command_handler.Register_Command("multiply", MultiplyCommand())
        logger.info("Command 'multiply' registered.")
        self.command_handler.Register_Command("divide", DivideCommand())
        logger.info("Command 'divide' registered.")

    def test_registered_commands(self):
        """Ensure all commands are properly registered."""
        logger.debug("Running test for registered commands...")
        expected_commands = ["add", "subtract", "multiply", "divide"]
        registered_commands = self.command_handler.get_registered_commands()
        logger.debug("Registered commands: %s", registered_commands)
        self.assertListEqual(sorted(registered_commands), sorted(expected_commands))

    def test_execute_add(self):
        """Test addition command execution."""
        logger.debug("Running test for add command execution...")
        result = self.command_handler.Execute_Command("add", "3", "2")
        logger.debug("Result of add: %s", result)
        self.assertEqual(result, 5)

    def test_execute_subtract(self):
        """Test subtraction command execution."""
        logger.debug("Running test for subtract command execution...")
        result = self.command_handler.Execute_Command("subtract", "10", "4")
        logger.debug("Result of subtract: %s", result)
        self.assertEqual(result, 6)

    def test_execute_multiply(self):
        """Test multiplication command execution."""
        logger.debug("Running test for multiply command execution...")
        result = self.command_handler.Execute_Command("multiply", "3", "4")
        logger.debug("Result of multiply: %s", result)
        self.assertEqual(result, 12)

    def test_execute_divide(self):
        """Test division command execution."""
        logger.debug("Running test for divide command execution...")
        result = self.command_handler.Execute_Command("divide", "10", "2")
        logger.debug("Result of divide: %s", result)
        self.assertEqual(result, 5)

    def test_execute_divide_by_zero(self):
        """Ensure division by zero is handled properly."""
        logger.debug("Running test for divide by zero...")
        result = self.command_handler.Execute_Command("divide", "5", "0")
        logger.debug("Result of divide by zero: %s", result)
        self.assertIsNone(result)

    def test_invalid_command(self):
        """Ensure an invalid command is not executed."""
        logger.debug("Running test for invalid command execution...")
        result = self.command_handler.Execute_Command("unknown_command", "5", "2")
        logger.debug("Result of unknown command: %s", result)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
