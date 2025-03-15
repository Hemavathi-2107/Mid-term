from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand
from app.history.calculation_history import display_history, clear_history, delete_record

# A list to store registered commands for display
registered_commands = []

def register_command(command):
    """Function to register commands and store them in the registered_commands list."""
    registered_commands.append(command)
    print(f"Command '{command}' registered.")

def repl():
    print("Welcome to the calculator! Enter a command to interact with the calculation history.")
    
    # Display all registered commands
    print("\nRegistered commands:")
    for command in registered_commands:
        print(command)
    
    while True:
        command = input(">>> ").strip()
        
        if command.lower() == 'exit':
            print("Exiting...Goodbye..")
            break
        
        elif command.lower() == 'show history':
            display_history()
        
        elif command.lower() == 'clear history':
            clear_history()
        
        elif command.lower().startswith('delete'):
            _, index = command.split(' ')
            delete_record(int(index))
        
        elif command.lower().startswith('add'):
            _, *args = command.split(' ')
            result = AddCommand().execute(*args)
            if result is not None:
                print(f"Result: {result}")
        
        elif command.lower().startswith('sub'):
            _, *args = command.split(' ')
            result = SubtractCommand().execute(*args)
            if result is not None:
                print(f"Result: {result}")
        
        elif command.lower().startswith('mul'):
            _, *args = command.split(' ')
            result = MultiplyCommand().execute(*args)
            if result is not None:
                print(f"Result: {result}")
        
        elif command.lower().startswith('div'):
            _, *args = command.split(' ')
            result = DivideCommand().execute(*args)
            if result is not None:
                print(f"Result: {result}")
        
        else:
            print("Unknown command. Type 'exit' to quit.")

def save_history(expression, result):
    """Function to save a calculation to the history file."""
    from app.history.calculation_history import save_history  # Import save function here
    save_history(expression, result)

if __name__ == "__main__":
    # Register commands
    register_command('add')
    register_command('subtract')
    register_command('multiply')
    register_command('divide')
    register_command('show history')
    register_command('clear history')
    register_command('delete')
    register_command('exit')
    repl()
