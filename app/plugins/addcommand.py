
import logging
from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Add(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler
        
    def execute(self, *args):
        if not args:  # Prompts for input if arguments are not given
            args = input("Enter two numbers separated by space: ").split()
        if len(args) != 2:  # Ensures exactly two arguments are given
            logging.warning("Only two arguments must be given")
            print("Only two arguments must be given")
            return

        try:
            x, y = map(Decimal, args)  
            result = Calculator.add(x, y)
            logging.info(f"Adding {x} and {y}, result: {result}")
            print(f"{x} + {y} = {result}")
        except InvalidOperation:
            logging.error("One of the entered numbers is invalid. Please enter valid inputs.")
            print("One of the entered numbers is invalid. Please enter valid inputs.")
        except Exception as e:
            logging.error(f"Error: {e}")
            print(f"Error: {e}")
