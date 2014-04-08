# Main instance of <Money in the Bank>


# IMPORTS
import sql_manager
from re import search
import hashlib
from string import punctuation
from getpass import getpass
from time import time
from smtplib import SMTP


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")
    while True:
        command = input("$$$>")
        if command == 'register':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            email = input("Enter your email: ")
            if check_password(password) is True:
                password = _generate_hash_pw(password)
                sql_manager.register(username, password, email)
                print("Registration Successfull")
            else:
                print("Your password sucks. Think of a better one and try to register again.")

        elif command == 'login':
            username = input("Enter your username: ")
            if abs(time() - sql_manager.get_current_time(username)) > 300:
                sql_manager.reset_failed_logins()
            if sql_manager.get_attempts(username) < 21:
                password = getpass("Enter your password: ")
                password = _generate_hash_pw(password)
                logged_user = sql_manager.login(username, password)
                if logged_user:
                    sql_manager.reset_failed_login(username)
                    logged_menu(logged_user)
                else:
                    sql_manager.failed_login(username)
                    print("Login failed")
            else:
                print("Number of login attempts(20) exceeded. Wait 5 minutes before attempting to login.")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("send-reset-password - sends a reset code to a gmail.")
            print("reset-password - resets the password if the entered code matches the received code.")
            print("exit - for closing program!")

        elif command == 'exit':
            break

        elif command == "send-reset-password":
            username = input("Enter your username: ")
            gmail_username = input("Gmail username: ")
            gmail_password = getpass("Gmail password: ")
            gmail_email = sql_manager.get_email(username)
            smtp_server = SMTP("smtp.gmail.com", 587)
            smtp_server.ehlo()
            smtp_server.starttls()
            smtp_server.login(gmail_username, gmail_password)
            reset_code = _generate_hash_pw(username)
            TEXT = "Use <reset-password> and enter this code <{}> without the brackets to reset your password.".format(reset_code)
            BODY = '\r\n'.join(['To: {}'.format(gmail_email),
                    'From: money-in-the-bank@awesome-app.com',
                    'Subject: Your Password Reset for username {}'.format(username),
                    '', TEXT])
            try:
                smtp_server.sendmail("money-in-the-bank@awesome-app.com", gmail_email, BODY)
                print ('Email sent.')
            except Exception as e:
                print(e)
                print ('Error sending mail.')
            smtp_server.quit()
            sql_manager.add_reset_code(username, reset_code)

        elif command == "reset-password":
            username = input("Enter your username: ")
            received_code = input("Reset code: ")
            if received_code == sql_manager.get_reset_code(username):
                print("Codes match!")
                new_password = getpass("Your new password: ")
                new_password = _generate_hash_pw(new_password)
                try:
                    sql_manager.change_pass_by_username(username, new_password)
                except Exception as e:
                    print(e)
                    print("No such username.")
                print("Password changed.")
        else:
            print("Not a valid command.")


def check_password(password):
    if len(password) > 8:
        if search('\d+', password):
            if search('[a-z]', password) and search('[A-Z]', password):
                for char in password:
                    if char in set(punctuation):
                        return True
    return False


def _generate_hash_pw(password):
    pw = hashlib.sha1()
    pw.update(password.encode("utf-8"))
    return pw.hexdigest()


def check_hash_password(password, hash_password):
    return _generate_hash_pw(password) == hash_password


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = getpass("Enter your new password: ")
            if check_password(new_pass) is True:
                new_pass = _generate_hash_pw(new_pass)
                sql_manager.change_pass(new_pass, logged_user)
            else:
                print("Your password sucks. Think of a better one!")

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("exit - exits. Duh.")


# main
def main():
    sql_manager.create_clients_table()
    main_menu()


# PROGRAM RUN
if __name__ == '__main__':
    main()
