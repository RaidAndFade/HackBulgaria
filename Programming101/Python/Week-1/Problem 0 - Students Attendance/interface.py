# Interface for attendance.py


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

    def callback_create_attendance_file(self, arguments):
        if self.fh.create_attendance_file() is True:
            return "New file created and loaded: {}".format(self.fh.get_current_open_file())
        elif self.fh.create_attendance_file() is False:
            return "You already have a file for today it is: {}".format(self.fh.get_current_open_file())

    def callback_change_current_date(self, arguments):
        if self.fh.change_current_date(arguments) is True:
            return "Date changed to {}/{}/{}\nCurrent file saved & discarded.\nYou can create or load.".format(arguments[0], arguments[1], arguments[2])

    def callback_add_attendance(self, arguments):
        try:
            student = "{} {}".format(arguments[0], arguments[1])
        except IndexError:
            return "Error: Please enter student as FirstName LastName"

        if self.fh.is_student_attending(student) is True:
            return "{} is already attending!".format(student)
        elif self.fh.is_student_attending(student) is False:
            if self.fh.add_attendance(student) is True:
                return "{} is now attending!".format(student)
            elif self.fh.add_attendance(student) is False:
                return "Create or load a file before adding!"
        elif self.fh.is_student_attending(student) is None:
            return "{} is not in our records.".format(student)

    def callback_list_files(self, arguments):
        return self.fh.list_attendance_files()

    def callback_help(self, arguments):
        help_message = ["Available commands are:", "* create", "* change_date", "* add", "* list", "* load", "* status", "* statistics"]
        return "\n".join(help_message)

    def callback_load(self, arguments):
        try:
            file_id = arguments[0]
        except IndexError:
            return "Error: No ID given"
        if self.fh.load_attendance_file(file_id) is True:
            return "Loaded {}".format(self.fh.get_current_open_file())
        elif self.fh.load_attendance_file(file_id) is False:
            return "Error: Invalid ID. Use list before using load."

    def callback_status(self, arguments):
        return self.fh.list_attending_students()

    def callback_statistics(self, arguments):
        return self.fh.get_statistics()

    def _init_callbacks(self):
        self.cp.on("create", self.callback_create_attendance_file)
        self.cp.on("change_date", self.callback_change_current_date)
        self.cp.on("add", self.callback_add_attendance)
        self.cp.on("list", self.callback_list_files)
        self.cp.on("help", self.callback_help)
        self.cp.on("load", self.callback_load)
        self.cp.on("status", self.callback_status)
        self.cp.on("statistics", self.callback_statistics)

    def _loop(self):
        while True:
            command = input("command>")
            self.cp.take_command(command)
