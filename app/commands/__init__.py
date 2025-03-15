import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Command(ABC):
    '''This is the abstract base class for commands.'''
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    '''This is the CommandHandler class.'''
    def __init__(self):
        self.commands = {}

    def Register_Command(self, command_name: str, command: Command):
        '''This function registers a command.'''
        self.commands[command_name] = command
        logging.info(f"Registered command: {command_name}")

    def Execute_Command(self, command_name: str, *args):
        '''Executes a registered command if it exists.'''
        try:
            if command_name in self.commands:
                logging.info(f"Executing command: {command_name} with arguments: {args}")
                return self.commands[command_name].execute(*args)
            else:
                logging.warning(f"{command_name}: Command not found")
        except (KeyError, TypeError) as e:
            logging.error(f"{command_name}: Invalid command or incorrect arguments provided - {e}")

    def get_registered_commands(self):
        '''Returns a list of registered commands.'''
        logging.info("Fetching list of registered commands")
        return list(self.commands.keys())