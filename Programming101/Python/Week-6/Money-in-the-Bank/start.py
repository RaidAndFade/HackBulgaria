# Main instance of <Money in the Bank>


# IMPORTS
import not_logged_functions
import logged_functions
from getpass import getpass


# FUNCTIONS
def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")
    while True:
        command = input("$$$>")
        if command == 'register':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            email = input("Enter your email: ")
            not_logged_functions.register(username, password, email)

        elif command == 'login':
            username = input("Enter your username: ")
            not_logged_functions.login(username)

        elif command == 'help':
            not_logged_functions.help()

        elif command == 'exit':
            break

        elif command == "send-reset-password":
            username = input("Enter your username: ")
            not_logged_functions.send_reset_password(username)

        elif command == "reset-password":
            not_logged_functions.reset_password()
        else:
            print("Not a valid command.")


def logged_menu(logged_user):
    username = logged_user.get_username()
    print("Welcome you are logged in as: " + username)
    while True:
        command = input("Logged>>")

        if command == 'info':
            logged_functions.info(logged_user)

        elif command == 'changepass':
            logged_functions.change_pass(logged_user)

        elif command == 'change-message':
            logged_functions.change_message(logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == "show-balance":
            print("Current balance: ${}".format(logged_user.get_balance()))

        elif command == "withdraw":
            logged_functions.withdraw(logged_user)

        elif command == "deposit":
            logged_functions.deposit(logged_user)

        elif command == "send-tan-codes":
            logged_functions.send_tan_codes(logged_user)

        elif command == 'help':
            logged_functions.help()

        elif command == 'logout':
            break


def main():
    not_logged_functions.prepare_db()
    main_menu()


# PROGRAM RUN
if __name__ == '__main__':
    main()
