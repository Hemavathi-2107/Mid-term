
from app.commands import Command

class DivideCommand(Command):
    '''Command to perform division.'''
    def execute(self, *args):
        try:
            numbers = list(map(float, args))
            if len(numbers) < 2:
                print("Error: Division requires at least two numbers.")
                return None
            result = numbers[0]
            for num in numbers[1:]:
                if num == 0:
                    print("Error: Division by zero is not allowed.")
                    return None
                result /= num
            return int(result) if result.is_integer() else result
        except ValueError:
            print("Error: Invalid input. Please enter numbers.")
            return None
