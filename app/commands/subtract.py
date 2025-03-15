from app.commands import Command
from app.history.calculation_history import save_history

class SubtractCommand(Command):
    '''Command to perform subtraction.'''
    def execute(self, *args):
        try:
            # Join all args to recreate the expression as a string (e.g., "5 - 2")
            expression = " - ".join(args)
            
            # Convert input arguments to float and calculate the result
            numbers = list(map(float, args))
            result = numbers[0] - sum(numbers[1:])
      
            # Save the history (pass the expression and result)
            save_history(expression, result)
            
            # Return the result as an int if it's a whole number, else as a float
            return int(result) if result.is_integer() else result
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
            return None
