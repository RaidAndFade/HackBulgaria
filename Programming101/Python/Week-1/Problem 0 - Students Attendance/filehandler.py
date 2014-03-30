# Handles file-related tasks for attendance.py


# IMPORTS
from glob import glob
from time import time
from datetime import datetime


class FileHandler():
    """docstring for FileHandler"""
    def __init__(self):
        self.attending_students = []
        self.files = []
        self.registered_students = self.read_registered_students()
        self.current_date = datetime.fromtimestamp(time()).strftime('%Y_%m_%d')
        self.current_open_file = ""

    def read_registered_students(self):
        opened_file = open("students", "r")
        contents = []
        for line in opened_file:
            contents.append(line.strip())
        opened_file.close()
        return contents

    def add_attendance(self, student):
        if self.current_open_file == "":
            return False
        self.attending_students.append(student)
        opened_file = open(self.current_open_file, "a")
        opened_file.write("{}\n".format(student))
        opened_file.close()
        return True

    def is_student_attending(self, student):
        if student in self.attending_students:
            return True
        elif student in self.registered_students:
            return False
        return None

    def get_current_open_file(self):
        return self.current_open_file

    def create_attendance_file(self):
        filename = "attendance_{}".format(self.current_date)
        if filename == self.current_open_file:
            return False
        opened_file = open(filename, "a")
        for student in self.attending_students:
            opened_file.write("{}\n".format(student))
        opened_file.close()
        self.current_open_file = filename
        return True

    def change_current_date(self, new_date):
        # format current_date for create_attendance_file
        new_date = "%s_%s_%s" % (new_date[2], new_date[1], new_date[0])
        self.current_date = new_date
        self.current_open_file = ""
        self.attending_students.clear()
        return True

    def list_attendance_files(self):
        list_output = []
        # clearing files before updating
        self.files.clear()
        for i, file in enumerate(glob('attendance_*')):
            self.files.append(file)
            list_output.append("[{}] - {}".format(i+1, file))
        return "\n".join(list_output)

    def list_attending_students(self):
        list_output = []
        for i, student in enumerate(self.attending_students):
            list_output.append("{}. {}".format(i+1, student))
        return "\n".join(list_output)

    def load_attendance_file(self, file_id):
        try:
            self.current_open_file = self.files[int(file_id)-1]
        except IndexError:
            return False
        opened_file = open(self.current_open_file, "r")
        for line in opened_file:
            self.attending_students.append(line.strip())
        opened_file.close()
        return True

    def get_statistics(self):
        # get total registered
        total_registered_students = len(self.registered_students)
        list_output = []
        # update files list before getting stats
        self.list_attendance_files()
        for filename in self.files:
            opened_file = open(filename, "r")
            file_students_attending = 0
            for line in opened_file:
                file_students_attending += 1
            filename = filename[11:].replace("_", "-")
            stats = "File: {} - {} attending from total of {} students".format(filename, file_students_attending, total_registered_students)
            list_output.append(stats)
            opened_file.close()
        return "\n".join(list_output)
