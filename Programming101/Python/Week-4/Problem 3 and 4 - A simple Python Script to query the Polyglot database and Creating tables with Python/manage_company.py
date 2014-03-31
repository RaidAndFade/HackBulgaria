# DOCUMENTATION


# IMPORTS
import command_handler


# main
def main():
    main_interface = command_handler.CommandHandler("polyglot.db")

    while True:
        command = main_interface.parse_command(str(input("Enter command>")))

        if main_interface.is_command(command, "help"):
            print(main_interface.trigger_help())

        elif main_interface.is_command(command, "list_employees"):
            print(main_interface.trigger_list_employees())

        elif main_interface.is_command(command, "monthly_spending"):
            print("The company is spending ${} every month!".format(main_interface.trigger_monthly_spending()))

        elif main_interface.is_command(command, "yearly_spending"):
            print("The company is spending ${} every year!".format(main_interface.trigger_yearly_spending()))

        elif main_interface.is_command(command, "add_employee"):
            main_interface.trigger_add_employee()

        elif main_interface.is_command(command, "delete_employee"):
            print(main_interface.trigger_delete_employee(command[1]))

        elif main_interface.is_command(command, "update_employee"):
            main_interface.trigger_update_employee(command[1])

        else:
            print(main_interface.trigger_unknown_command())


# PROGRAM RUN
if __name__ == "__main__":
    main()
