from calculator.commands import Command
class DivideCommand(Command):
    def __init__(self, command_handler):
        super().__init__()
        self.command_handler = command_handler

    def execute(self, arg1, arg2):
        if arg2 == 0:
            raise ValueError("Cannot divide by zero.")
        return arg1 / arg2