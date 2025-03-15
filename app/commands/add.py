from app.commands import Command

class AddCommand(Command):
    '''Command to perform addition.'''
    def execute(self, *args):
        try:
            numbers = list(map(float, args))  # Convert input arguments to float
            result = sum(numbers)
            return int(result) if result.is_integer() else result  # Convert to int if whole number
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
            return None