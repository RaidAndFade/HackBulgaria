# DOCUMENTATION
# https://github.com/syndbg/HackBulgaria/tree/master/Programming101/Python/Week-1/Problem%200%20-%20Students%20Attendance


# IMPORTS
import os
import re
from time import time
from datetime import datetime


# FUNCTIONS
def parse_command(command):
    # return tuple(command.split(" "))
    # changed to handle dates better
    return tuple(re.split('[/ ]', command))


def is_command(command_tuple, command_string):
    return command_tuple[0] == command_string


def trigger_command_add(command_tuple):
    if len(command_tuple) != 3:
        print("Please enter student as: FirstName LastName")
        return

    student = "%s %s" % (command_tuple[1], command_tuple[2])
    file = open("students", "r")
    for line in file:
        if student in attending_students:
            print("%s is already attending!" % student)
            return

        if student in line:
            print("%s is now attending!" % student)
            attending_students.append(student)
            return True

    print("%s is not in our records" % student)
    return False


def trigger_command_create():
    filename = "attendance_%s" % current_date
    #current_open_file = "attendance_%s" % current_date

    # appending if existing, but not clearing and writing anew!
    file = open(filename, "a")
    for student in attending_students:
        file.write("%s\n" % student)
    file.close()
    print("New file created and loaded:", filename)


def trigger_command_change_date(command_tuple):
    # format current_date for trigger_command_create
    global current_date
    current_date = "%s_%s_%s" % (command_tuple[3], command_tuple[2], command_tuple[1])
    print("Changed current date to %s/%s/%s" % (command_tuple[1], command_tuple[2], command_tuple[3]))


def trigger_command_list():
    i = 0
    for file in os.listdir('.'):
        if file.startswith("attendance_"):
            i += 1
            files.append(file)
            print("[%s] - %s" % (i, file))


def trigger_command_load(command_tuple):
    if len(command_tuple) != 2:
        print("Error: Invalid number of arguments given!")
        return

    current_open_file = files[int(command_tuple[1])-1]
    print("File %s loaded!" % current_open_file)
    global attending_students
    # clear list
    attending_students[:] = []

    file = open(current_open_file, "r")
    for line in file:
        attending_students.append(line.rstrip())
    file.close()
    return


def trigger_command_status():
    for i in range(len(attending_students)):
        # it's.. fancy!
        fancy_index = i + 1
        print("%s. %s" % (fancy_index, attending_students[i]))


def trigger_command_statistic():
    # get total registered
    total_registered_students = 0
    students_file = open("students", "r")
    for line in students_file:
        total_registered_students += 1

    # bug: must have used list before statistic or else it doesn't work.
    for file in files:
        file = open(file, "r")
        file_students_attending = 0
        for line in file:
            file_students_attending += 1
        print("File: %s - %s attending from total of %s students" % (file, file_students_attending, total_registered_students))
        file.close()


def trigger_unknown_command():
    unknown_command = ["Error: Unknown command!",
                       "Available commands are:",
                       "create", "change_date",
                       "add", "list", "load",
                       "status", "statistics"]

    return "\n".join(unknown_command)


# Must be global!
# Stores date (current date unless modified)
ts = time()
current_date = datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
# Current loaded file's attending students
attending_students = []
# All files in directory. Will be updated only if list is used!
files = []


# main
def main():
    while True:
        command = parse_command(input("Enter a command> "))

        if is_command(command, "create"):
            trigger_command_create()

        elif is_command(command, "change_date"):
            trigger_command_change_date(command)

        elif is_command(command, "add"):
            trigger_command_add(command)

        elif is_command(command, "list"):
            trigger_command_list()

        elif is_command(command, "load"):
            trigger_command_load(command)

        elif is_command(command, "status"):
            trigger_command_status()

        elif is_command(command, "statistic"):
            trigger_command_statistic()

        else:
            print(trigger_unknown_command())


# PROGRAM RUN
if __name__ == "__main__":
    main()
