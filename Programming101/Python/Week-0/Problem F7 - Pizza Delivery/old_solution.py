# Problem F7 - Pizza delivery
# https://github.com/HackBulgaria/Programming101/blob/master/week0/simple_problems3.md#problem-f7---pizza-delivery


# IMPORTS
from sys import exit
from time import time
from datetime import datetime


# FUNCTIONS
def parse_command(command):
    return tuple(command.split(" "))


def is_command(command_tuple, command_string):
    return command_tuple[0] == command_string


def trigger_take(command_tuple):
    if len(command_tuple) == 3:
        print("Taking order from %s for %s" % (command_tuple[1], command_tuple[2]))
        orders[command_tuple[1]] = command_tuple[2]
        history.append(command_tuple[0])
    else:
        print("Error command take: not enough arguments given!")


def trigger_save(command_tuple):
    ts = time()
    filename = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
    files.append(filename)
    file = open(filename, "w")

    for item in orders:
        file.write("%6s - %s" % (item, orders[item]))
        file.write("\n")

    # clear orders and add save as last valid command used
    orders.clear()
    history.append(command_tuple[0])


def trigger_status(command_tuple):
    if len(orders) == 0:
        print("Orders dictionary is empty.")
    else:
        for item in orders:
            print("%6s - %s" % (item, orders[item]))
        history.append(command_tuple[0])


def trigger_list(command_tuple):
    for i in range(len(files)):
        print("[%s] - %s" % (i + 1, files[i]))

    history.append(command_tuple[0])


def trigger_load(command_tuple):
    try:
        if len(command_tuple) != 2:
            print("Error command load: Invalid number of arguments")

        elif len(command_tuple) == 2:
            if history[-1] != "list":
                print("Use list command before loading files.")

            elif history[len(history) - 1] == "list":
                    elementIndex = int(command_tuple[1]) - 1
                    filename = files[elementIndex]
                    print("Loaded %s" % filename)
                    file = open(filename, "r")
                    contents = file.read()
                    print(contents)
            else:
                print("Use list command before loading files.")

    except IndexError:
        print("Error: Invalid argument.")
        return


def trigger_history(history_list):
    print(history_list)


def trigger_finish(command_tuple):
    if len(history) != 0:
        if history[len(history)-1] != "save":
            print("You have not saved your order")
            print("If you wish to continue exiting, type finish again")
            print("If you want to save your order, type save")

            # confirm finish
            command_tuple = parse_command(input("Enter command>"))
            if is_command(command_tuple, "finish"):
                exit("Command finish, confirmed. Exiting.")
    else:
        exit("No commands entered beforehand. Exiting.")


def trigger_unknown_command():
    unknown_command = ["Error: Unknown command!",
                       "Try one of the following:",
                       " take <name> <price>",
                       " status",
                       " save",
                       " list",
                       " load <number>",
                       " finish"]

    print("\n".join(unknown_command))


# must be global!
# history - will store the orders before they're exported to files
history = []
# orders - will store the file names where the orders were exported
orders = {}
# files - will store all the VALID commands entered and
# will be used for previous command conditions
files = []


# main
def main():
    while True:
        command = parse_command(input("Enter command>"))

        if is_command(command, "take"):
            trigger_take(command)

        elif is_command(command, "status"):
            trigger_status(command)

        elif is_command(command, "save"):
            trigger_save(command)

        elif is_command(command, "list"):
            trigger_list(command)

        elif is_command(command, "load"):
            trigger_load(command)

        elif is_command(command, "finish"):
            trigger_finish(command)

        # easter egg
        elif is_command(command, "history"):
            trigger_history(history)

        else:
            trigger_unknown_command()


# PROGRAM RUN
if __name__ == '__main__':
    main()
