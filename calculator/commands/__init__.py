import logging
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        self.commands[name] = command
        logging.info(f"Command '{name}' has been registered.")
    
     # Add this method to return a list of registered commands
    def get_registered_commands(self):
        return f"{list(self.commands.keys())}"   # Return the list of command names

    def execute_command(self, name, arg1, arg2):
        if name in self.commands:
            try:
                return f"{self.commands[name].execute(arg1, arg2)}"
            except ValueError as e:
                logging.error(e)
                  # Return the error message to the user
        else:
            logging.error(f"No such command: '{name}'")
           

