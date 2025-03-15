from app.commands import Command
from app.history.calculation_history import save_history

class MultiplyCommand(Command):
    '''Command to perform multiplication.'''
    def execute(self, *args):
        try:
            # Join all args to recreate the expression as a string (e.g., "5 * 6")
            expression = " * ".join(args)
            
            # Convert input arguments to float and calculate the product
            numbers = list(map(float, args))
            result = 1
            for number in numbers:
                result *= number
     
            # Save the history (pass the expression and result)
            save_history(expression, result)
            
            # Return the result as an int if it's a whole number, else as a float
            return int(result) if result.is_integer() else result
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
            return None
