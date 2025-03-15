
from app.commands import Command

class SubtractCommand(Command):
    '''Command to perform subtraction.'''
    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            result = numbers[0] - sum(numbers[1:])  # Subtract all subsequent numbers from the first
            return int(result) if result.is_integer() else result
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
            return None
        except IndexError:
            print("Error: Subtraction requires at least one number.")
            return None
