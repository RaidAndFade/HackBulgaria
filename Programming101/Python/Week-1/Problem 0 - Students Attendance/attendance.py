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


def trigger_command_add(command_tuple, attending_students):
    if len(command_tuple) != 3:
        print("Please enter student as: FirstName LastName")
        return

    student = "%s %s" % (command_tuple[1], command_tuple[2])
    students_file = open("students", "r")
    for line in students_file:
        if student in attending_students:
            print("%s is already attending!" % student)
            students_file.close()
            return

        if student in line:
            print("%s is now attending!" % student)
            attending_students.append(student)
            students_file.close()
            return True

    students_file.close()
    print("%s is not in our records." % student)
    return False


def trigger_command_create(current_date, attending_students):
    filename = "attendance_%s" % current_date
    #current_open_file = "attendance_%s" % current_date

    # appending if existing, but not clearing and writing anew!
    file = open(filename, "a")
    for student in attending_students:
        file.write("%s\n" % student)
    file.close()
    print("New file created and loaded:", filename)


def trigger_command_change_date(command_tuple, current_date):
    # format current_date for trigger_command_create
    current_date = "%s_%s_%s" % (command_tuple[3], command_tuple[2], command_tuple[1])
    print("Changed current date to %s/%s/%s" %
          (command_tuple[1], command_tuple[2], command_tuple[3]))
    return current_date


def trigger_command_list(files):
    list_output = []
    i = 0
    for file in os.listdir('.'):
        if file.startswith("attendance_"):
            i += 1
            files.append(file)
            # print("[%s] - %s" % (i, file))
            list_output.append("[%s] - %s" % (i, file))

    # update files to current listed
    files = list_output
    return "\n".join(list_output)


def trigger_command_load(command_tuple, files, attending_students):
    if len(command_tuple) != 2:
        print("Error: Invalid number of arguments given!")
        return

    current_open_file = files[int(command_tuple[1]) - 1]
    print("File %s loaded!" % current_open_file)
    # clear list
    attending_students[:] = []

    file = open(current_open_file, "r")
    for line in file:
        attending_students.append(line.rstrip())
    file.close()

    return


def trigger_command_status(attending_students):
    list_output = []
    for i in range(len(attending_students)):
        # it's.. fancy!
        fancy_index = i + 1
        # print("%s. %s" % (fancy_index, attending_students[i]))
        list_output.append("%s. %s" % (fancy_index, attending_students[i]))

    return "\n".join(list_output)


def trigger_command_statistic(files):
    # get total registered
    total_registered_students = 0
    students_file = open("students", "r")
    for line in students_file:
        total_registered_students += 1

    # FIXED! bug: must have used list before statistic or else it doesn't work.
    list_output = []
    # update files list before getting stats
    trigger_command_list(files)

    for filename in files:
        file = open(filename, "r")
        file_students_attending = 0
        for line in file:
            file_students_attending += 1
        stats = "File: %s - %s attending from total of %s students" % (
            filename, file_students_attending, total_registered_students)

        list_output.append(stats)
        file.close()

    return "\n".join(list_output)


def trigger_unknown_command():
    unknown_command = ["Error: Unknown command!",
                       "Available commands are:",
                       "create", "change_date",
                       "add", "list", "load",
                       "status", "statistic"]

    return "\n".join(unknown_command)


# main
def main():
    # Stores date (current date unless modified)
    ts = time()
    current_date = datetime.fromtimestamp(ts).strftime('%Y_%m_%d')
    # Current loaded file's attending students
    attending_students = []
    # All files in directory. Will be updated only if list is used!
    files = []

    while True:
        command = parse_command(input("Enter a command> "))

        if is_command(command, "create"):
            trigger_command_create(current_date, attending_students)

        elif is_command(command, "change_date"):
            current_date = trigger_command_change_date(command, current_date)

        elif is_command(command, "add"):
            trigger_command_add(command, attending_students)

        elif is_command(command, "list"):
            print(trigger_command_list(files))

        elif is_command(command, "load"):
            trigger_command_load(command, files, attending_students)

        elif is_command(command, "status"):
            print(trigger_command_status(attending_students))

        elif is_command(command, "statistic"):
            print(trigger_command_statistic(files))

        else:
            print(trigger_unknown_command())


# PROGRAM RUN
if __name__ == "__main__":
    main()
