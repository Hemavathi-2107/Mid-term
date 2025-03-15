from app.commands import Command
from app.history.calculation_history import save_history

class DivideCommand(Command):
    '''Command to perform division.'''
    def execute(self, *args):
        try:
            # Join all args to recreate the expression as a string (e.g., "6 / 2")
            expression = " / ".join(args)
            
            # Convert input arguments to float and calculate the result
            numbers = list(map(float, args))
            if numbers[1] == 0:
                print("Error: Division by zero is not allowed.")
                return None
            result = numbers[0] / numbers[1]
            
             
            # Save the history (pass the expression and result)
            save_history(expression, result)
            
            # Return the result as an int if it's a whole number, else as a float
            return int(result) if result.is_integer() else result
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
            return None
