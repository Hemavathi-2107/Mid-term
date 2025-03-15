import logging
from app.commands import Command

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Menu(Command):
    '''This displays available commands in the system'''
   
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self, *args):
        commands = self.command_handler.Get_Registered_Commands()

        if not commands:
            logging.warning("No commands available in the system.")
            print("There are no commands")
            return

        logging.info("Displaying available commands.")
        print("Commands Available:")
        for command in commands:
            print(f"-> {command}") 
        print("Type 'exit' to quit")