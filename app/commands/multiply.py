
from app.commands import Command

class MultiplyCommand(Command):
    '''Command to perform multiplication.'''
    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            result = 1
            for num in numbers:
                result *= num
            return int(result) if result.is_integer() else result
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
            return None
