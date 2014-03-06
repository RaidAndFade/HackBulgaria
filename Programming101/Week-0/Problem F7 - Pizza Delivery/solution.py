# Problem F7 - Pizza delivery
#
# Implement a Python program, called pizza.py that will help us organize the pizza ordering!
#
# We are going to implement a program, that waits for commands from the user and acts on them. Some commands may affect other commands and the program loops forever, until finish command is issued.
#
# We are going to take input in Python like that:
#
# command = input("Enter command>")
# Here is an example start of the program:
#
# $ python pizza.py
# Enter command>
# The user can enter one of the following commands:
#
# take <name> <price>
# status
# save
# list
# load <number>
# finish
# Now let's go through each of the commands:
#
# take
#
# The take commands followed by a name and a price, adds the given Person with the given prices to the current order.
#
# One person can take many things, adding up to the total price for him.
#
# For example:
#
# Enter command>take Rado 10.0
# Taking order from Rado for 10.00
# Enter command>take Rado 10
# Taking order from Rado for 10.00
# Enter command>take Ivan 6.43
# Taking order from Ivan for 6.43
# Enter command>take Maria 7.50
# Taking order from Maria for 7.50
# Enter command>
# status:
#
# The status command prints the current status of the order in the following format for each person:
#
# Person - Total Sum
# For example:
#
# Enter command>take Rado 10.0
# Taking order from Rado for 10.00
# Enter command>take Rado 10
# Taking order from Rado for 10.00
# Enter command>take Ivan 6.43
# Taking order from Ivan for 6.43
# Enter command>take Maria 7.50
# Taking order from Maria for 7.50
# Enter command>status
# Rado - 20.00
# Ivan - 6.43
# Maria - 7.50
# Enter command>
# save:
#
# We should be able to save the current order in a file!
#
# When we issue the save command, the script should do the following:
#
# Create a timestamped file, named orders_YYYY_mm_dd_hh_mm_ss where YYYY is the current year, mm the current month, dd the current day, hh the current hour, mm the current minutes and ss the current seconds.
# You can achieve the timestamp with the following code:
#
# from time import time
# from datetime import datetime
#
# ts = time()
# stamp = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
# Save the current order in that file. The formating of the current order should be the same formatting, when printing it with the status command.
#
# After the file is saved, keep taking orders (Don't quit the program)
#
# list:
#
# The list command shows all files with saved orders in the current directory.
#
# When displaying them, it adds unique number to each file, starting from one. This number will be used in the load command.
#
# See this example, where we do two saves and call list after that:
#
# Enter command>take Ivan 10
# Taking order from Ivan for 10.00
# Enter command>take Maria 5.50
# Taking order from Maria for 5.50
# Enter command>take Rado 6.10
# Taking order from Rado for 6.10
# Enter command>save
# Saved the current order to orders_2014_03_01_11_00_00
# Enter command>take Maria 10.50
# Taking order from Maria for 10.50
# Enter command>save
# Saved the current order to orders_2014_03_01_11_00_08
# Enter command>list
# [1] - orders_2014_03_01_11_00_08
# [2] - orders_2014_03_01_11_00_00
# Enter command>
#
# load :
#
# The load command discards the current order and loads a saved one from a file. A second argument, a number, is given. This is the unique number for the file, showed in the list command.
#
# The algorithm for load is:
#
# If you call load before list, a message is displayed : Use list command before loading
# If you load a file and the current order is not saved (Changes have been made after the last save or no save at all) - The program should display a warning message :
# You have not saved the current order.
# If you wish to discard it, type load <number> again.
# If you type load <number> again, the current order is discarded and it's replaced by the one saved in the file. You have to parse the file for that.
#
# If you call load and you have an empty current order, you should load the file without a problem.
#
# Check the examples:
#
# Loading without save:
#
# Enter command>take Rado 10
# Taking order from Rado for 10.00
# Enter command>take Maria 5.50
# Taking order from Maria for 5.50
# Enter command>list
# [1] - orders_2014_03_01_11_00_08
# [2] - orders_2014_03_01_11_00_00
# Enter command>load 1
# You have unsaved order.
# If you wish to discard the current order, type load again
# Enter command>
# Loading order:
#
# $ cat orders_2014_03_01_11_00_00
# Maria - 5.50
# Ivan - 10.00
# Rado - 6.10
# $ py pizza.py
# Enter command>list
# [1] - orders_2014_03_01_11_00_08
# [2] - orders_2014_03_01_11_00_00
# Enter command>load 2
# Loading orders_2014_03_01_11_00_00
# Enter command>status
# Maria - 5.50
# Rado - 6.10
# Ivan - 10.00
# Enter command>
#
# finish:
#
# The finish command is for exiting the program.
#
# Here is the algorithm for finish:
#
# If you type finish and you have unsaved changes, you will get the following message:
# Enter command>finish
# You have not saved your order.
# If you wish to continue, type finish again.
# If you want to save your order, type save
# If you type finish again, the program will exit
# Enter command>finish
# Finishing order. Goodbye!
# $
# unknown command:
#
# If you type a command that is not supported by the program, print an error message.
#
# Something like this:
#
# Enter command>OMG
# Unknown command!
# Try one of the following:
# take <name> <price>
# status
# save
# list
# load <number>
# finish
# Enter command>

# IMPORTS
from sys import exit
from time import time
from datetime import datetime

# FUNCTIONS
# main
def main():
    # will store the orders before they're exported to files
    orders = { }
    # will store the file names where the orders were exported
    files = [ ]
    # will store all the VALID commands entered. Will be used for previous command conditions
    history = [ ]

    while True:
        # tuple for better performance (lol)
        knownCommands = ( "take", "status", "save", "list", "load", "finish", "history" )
        inputCommand = str(input("Enter a command> "))
        inputCommand = inputCommand.split(" ")

        # handle unknown commands
        if inputCommand[0] not in knownCommands:
            print("Unknown Command!")
            print("Try one of the following:\ntake <name> <price>\nstatus\nsave\nlist\nload <number>\nfinish")

        # handle finish
        elif inputCommand[0] == "finish":
            # when finish is the first command entered - just exit
            if len(history) == 0:
                exit("Nothing entered beforehand. Exiting...")

            elif history[len(history) - 1] != "save":
                print("You have not saved your order.")
                print("If you wish to continue type finish again")
                print("If you want to save your order, type save")

                # confirms finish (not the best implementation)
                inputCommand[0] = str(input("Enter a command> "))
                if inputCommand[0] == "finish":
                    exit("Command finish. Exiting...")

                # reused from save
                elif inputCommand[0] == "save":
                    ts = time()
                    filename = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
                    files.append(filename)
                    file = open(filename, "w")

                    for item in orders:
                            file.write("%10s - %s" % (item, orders[item]))
                            file.write("\n")

                    # clear orders
                    orders = { }
                    history.append(inputCommand[0])

        # handle take
        elif inputCommand[0] == "take":
            if len(inputCommand) == 3:
                print("Taking order from %s for %s" % (inputCommand[1], inputCommand[2]))
                orders[inputCommand[1]] = inputCommand[2]
                history.append(inputCommand[0])

        # handle status
        elif inputCommand[0] == "status":
            if len(orders) == 0:
                print("Empty orders list")
            else:
                for item in orders:
                    print("%6s - %s" % (item, orders[item]))
                history.append(inputCommand[0])

        # handle save
        elif inputCommand[0] == "save":
            ts = time()
            filename = datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            files.append(filename)
            file = open(filename, "w")

            for item in orders:
                    file.write("%6s - %s" % (item, orders[item]))
                    file.write("\n")

            # clear orders
            orders = { }
            history.append(inputCommand[0])


        # handle list
        elif inputCommand[0] == "list":
            for i in range(len(files)):
                print("[%s] - %s" % (i + 1, files[i]))
            history.append(inputCommand[0])

        # handle load
        elif inputCommand[0] == "load":
            if len(inputCommand) != 2:
                print("Invalid number of arguments")

            # check if list was used before load
            if history[len(history) - 1] != "list":
                print("Use list command before loading")
                break

            elementIndex = int(inputCommand[1]) - 1
            filename = files[elementIndex]
            file = open(filename, "r")
            contents = file.read()
            print(contents)

        # handle history (easter egg?)
        elif inputCommand[0] == "history":
            print(history)

# PROGRAM RUN
main()