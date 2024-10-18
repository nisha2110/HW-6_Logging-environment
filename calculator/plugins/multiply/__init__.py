from calculator.commands import Command
class MultiplyCommand(Command):
    def __init__(self, command_handler):
        super().__init__()
        self.command_handler = command_handler

    def execute(self, arg1, arg2):
        return arg1 * arg2
        