# Interface for pizza.py


# IMPORTS
from commandparser import CommandParser
from filehandler import FileHandler


class CLI():
    """docstring for CLI"""
    def __init__(self):
        self.cp = CommandParser()
        self.fh = FileHandler()
        self._init_callbacks()
        self._loop()

    def callback_take(self, arguments):
        try:
            name = arguments[0]
            price = int(arguments[1])
        except IndexError:
            return "Error: Give arguments as \"take <name> <price>\""
        if self.fh.take_order(name, price) is True:
            return "Taking order from {} for {}".format(name, price)

    def callback_status(self, arguments):
        return self.fh.list_orders()

    def callback_save(self, arguments):
        if self.fh.save_file() is True:
            return "Saved."

    def callback_list(self, arguments):
        return self.fh.list_files()

    def callback_load(self, arguments):
        try:
            list_id = int(arguments[0]) - 1
        except IndexError:
            return "Error: Invalid List ID."
        if self.fh.load_file(list_id) is None:
            return "Use list command before loading."
        elif self.fh.load_file(list_id) is False:
            return "You have not saved the current order.\nIf you wish to discard it, type load <number> again."
        elif self.fh.load_file(list_id) is True:
            return "Loaded {}.".format(self.fh.fetch_file_name(list_id))

    def callback_history(self, arguments):
        return self.fh.fetch_history()

    def callback_finish(self, arguments):
        return exit()

    def callback_help(self, arguments):
        help_message = ("Error: Unknown command!", "Try one of the following:", " take <name> <price>", " status", " save", " list", " load <number>", " finish")
        return "\n".join(help_message)

    def _init_callbacks(self):
        self.cp.on("take", self.callback_take)
        self.cp.on("status", self.callback_status)
        self.cp.on("save", self.callback_save)
        self.cp.on("list", self.callback_list)
        self.cp.on("load", self.callback_load)
        self.cp.on("finish", self.callback_finish)
        self.cp.on("help", self.callback_help)
        self.cp.on("history", self.callback_history)

    def _loop(self):
        while True:
            command = input("command>")
            self.cp.take_command(command)
