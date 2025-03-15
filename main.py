from app import CommandHandler, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

def main():
    # Create a command handler instance
    command_handler = CommandHandler()
    
    # Register commands
    command_handler.Register_Command("add", AddCommand())
    command_handler.Register_Command("subtract", SubtractCommand())
    command_handler.Register_Command("multiply", MultiplyCommand())
    command_handler.Register_Command("divide", DivideCommand())

    print("Welcome to the Command Pattern Calculator!")
    print("Type 'menu' to see the available commands.")
    
    while True:
        # Ask the user for a command input
        command_name = input("\nEnter command (or 'exit' to quit): ").strip().lower()

        if command_name == "exit":
            print("Exiting... Goodbye!")
            break
        elif command_name == "menu":
            # Display all registered commands
            available_commands = command_handler.get_registered_commands()
            print("Available commands:", ", ".join(available_commands))
        elif command_name in command_handler.get_registered_commands():
            try:
                # Ask for numbers from the user
                args = input(f"Enter the numbers separated by space for '{command_name}': ").strip().split()
                # Execute the command with the provided arguments
                result = command_handler.Execute_Command(command_name, *args)
                if result is not None:
                    print(f"Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"{command_name}: Command not found. Type 'menu' to see available commands.")

if __name__ == "__main__":
    main()