# Not logged menu functions


# IMPORTS
from start import logged_menu
from time import time
from getpass import getpass
import smtp_handler
import password_handler
import sql_manager


# FUNCTIONS
def prepare_db():
    sql_manager.create_clients_table()


def register(username, password, email):
    if password_handler.check_password(password) is True:
        password = password_handler._generate_hash_pw(password, "sha1")
        try:
            sql_manager.register(username, password, email)
        except Exception:
            print("Username already exists.")
            return
        print("Registration successful.")
    else:
        print("Your password sucks. Think of a better one and try again to register.")


def login(username):
    try:
        if abs(time() - sql_manager.get_current_time(username)) > 300:
                sql_manager.reset_failed_logins()
    except IOError:
        print("No such username.")
        return

    if sql_manager.get_attempts(username) < 21:
        password = getpass("Enter your password: ")
        password = password_handler._generate_hash_pw(password, "sha1")
        logged_user = sql_manager.login(username, password)
        if logged_user:
            sql_manager.reset_failed_login(username)
            logged_menu(logged_user)
        else:
            sql_manager.failed_login(username)
            print("Login failed")
    else:
        print("Number of login attempts(20) exceeded. Wait 5 minutes before attempting to login.")


def help():
    print("login - to log in!")
    print("register - create a new account!")
    print("send-reset-password - sends a reset code to a gmail.")
    print("reset-password - resets the password if the entered code matches the received code.")
    print("exit - closes the program!")


def send_reset_password(username):
    if smtp_handler.send_reset_code(username) is True:
        print("Sent you a reset code!")


def reset_password(username, received_code):
    username = input("Enter your username: ")
    smtp_handler.send_reset_code(username)
    received_code = input("Reset code: ")
    received_code = password_handler._generate_hash_pw(received_code, "sha224")
    if received_code == sql_manager.get_reset_code(username):
        print("Codes match!")
        new_password = getpass("Your new password: ")
        new_password = password_handler._generate_hash_pw(new_password, "sha1")
        try:
            sql_manager.change_pass_by_username(username, new_password)
        except Exception as e:
            print(e)
            print("No such username.")
            return
        print("Password changed.")
