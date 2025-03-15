
import logging
from app.commands import Command, CommandHandler
from app.commands.add import AddCommand
from app.commands.subtract import SubtractCommand
from app.commands.multiply import MultiplyCommand
from app.commands.divide import DivideCommand

# Configure the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize the CommandHandler
command_handler = CommandHandler()

# Register all available commands with logging
def register_commands():
    try:
        logger.info("Registering commands...")
        
        command_handler.Register_Command("add", AddCommand())
        logger.info("Command 'add' registered.")
        
        command_handler.Register_Command("subtract", SubtractCommand())
        logger.info("Command 'subtract' registered.")
        
        command_handler.Register_Command("multiply", MultiplyCommand())
        logger.info("Command 'multiply' registered.")
        
        command_handler.Register_Command("divide", DivideCommand())
        logger.info("Command 'divide' registered.")
    
    except Exception as e:
        logger.error(f"Error during command registration: {e}")

# Call the register_commands function to register commands
register_commands()

# Expose relevant components for external use
__all__ = ["command_handler", "Command"]
