# Main instance of <Money in the Bank>


# IMPORTS
import sql_manager
from re import search
import hashlib
from string import punctuation
from getpass import getpass
from time import time
from smtplib import SMTP
import gmail_config
from random_password_generator import generatePassword


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")
    while True:
        command = input("$$$>")
        if command == 'register':
            username = input("Enter your username: ")
            password = getpass("Enter your password: ")
            email = input("Enter your email: ")
            if check_password(password) is True:
                password = _generate_hash_pw(password, "sha1")
                try:
                    sql_manager.register(username, password, email)
                except Exception:
                    print("Username already exists.")
                print("Registration successful.")
            else:
                print("Your password sucks. Think of a better one and try to register again.")

        elif command == 'login':
            username = input("Enter your username: ")
            try:
                if abs(time() - sql_manager.get_current_time(username)) > 300:
                        sql_manager.reset_failed_logins()
                if sql_manager.get_attempts(username) < 21:
                    password = getpass("Enter your password: ")
                    password = _generate_hash_pw(password, "sha1")
                    logged_user = sql_manager.login(username, password)
                    if logged_user:
                        sql_manager.reset_failed_login(username)
                        logged_menu(logged_user)
                    else:
                        sql_manager.failed_login(username)
                        print("Login failed")
                else:
                    print("Number of login attempts(20) exceeded. Wait 5 minutes before attempting to login.")
            except IOError:
                print("No such username.")

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
            send_reset_code(username)

        elif command == "reset-password":
            username = input("Enter your username: ")
            received_code = input("Reset code: ")
            received_code = _generate_hash_pw(received_code, "sha224")
            if received_code == sql_manager.get_reset_code(username):
                print("Codes match!")
                new_password = getpass("Your new password: ")
                new_password = _generate_hash_pw(new_password, "sha1")
                try:
                    sql_manager.change_pass_by_username(username, new_password)
                except Exception as e:
                    print(e)
                    print("No such username.")
                print("Password changed.")
        else:
            print("Not a valid command.")


def _check_hash(received_code, true_code):
    return _generate_hash_pw(received_code, "sha224") == true_code


def send_reset_code(username):
    gmail_username = gmail_config.get_username()
    gmail_password = gmail_config.get_password()
    gmail_email = sql_manager.get_email(username)
    smtp_server = SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(gmail_username, gmail_password)
    reset_code = _generate_hash_pw(generatePassword(10), "sha1")
    TEXT = "Reset/confirmation code <{}>.".format(reset_code)
    BODY = '\r\n'.join(['To: {}'.format(gmail_email),
            'From: money-in-the-bank@awesome-app.com',
            'Subject: Your reset/confirmation code for username {}'.format(username),
            '', TEXT])
    try:
        smtp_server.sendmail("money-in-the-bank@awesome-app.com", gmail_email, BODY)
        print ('Email sent.')
    except Exception as e:
        print(e)
        print ('Error sending mail.')
    smtp_server.quit()
    reset_code = _generate_hash_pw(reset_code, "sha224")
    sql_manager.add_reset_code(username, reset_code)


def send_tan_codes(username):
    if sql_manager.are_available_tan_codes(username) is True:
        print("You have available TAN codes. Use them before you generate new ones.")
        return 0
    gmail_username = gmail_config.get_username()
    gmail_password = gmail_config.get_password()
    gmail_email = sql_manager.get_email(username)
    smtp_server = SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(gmail_username, gmail_password)
    tan_codes = []
    for i in range(10):
        tan_code = _generate_hash_pw(generatePassword(10), "sha224")
        tan_codes.append(tan_code)
    TEXT = "TAN CODES: {}.".format("\n".join(tan_codes))
    BODY = '\r\n'.join(['To: {}'.format(gmail_email),
            'From: money-in-the-bank@awesome-app.com',
            'Subject: Your TAN code for username {}'.format(username),
            '', TEXT])
    try:
        smtp_server.sendmail("money-in-the-bank@awesome-app.com", gmail_email, BODY)
        print ('Email sent.')
    except Exception as e:
        print(e)
        print ('Error sending mail.')
    smtp_server.quit()
    sql_manager.delete_tan_codes(username)
    for tan_code in tan_codes:
        tan_code = _generate_hash_pw(tan_code, "sha224")
        sql_manager.add_tan_code(username, tan_code)


def check_password(password):
    if len(password) > 8:
        if search('\d+', password):
            if search('[a-z]', password) and search('[A-Z]', password):
                for char in password:
                    if char in set(punctuation):
                        return True
    return False


def _generate_hash_pw(password, algorithm):
    if algorithm == "sha1":
        pw = hashlib.sha1()
    elif algorithm == "sha224":
        pw = hashlib.sha224()
    pw.update(password.encode("utf-8"))
    return pw.hexdigest()


def logged_menu(logged_user):
    username = logged_user.get_username()
    print("Welcome you are logged in as: " + username)
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            send_reset_code(username)
            received_code = input("The code you received: ")
            if sql_manager.get_reset_code(username) == received_code:
                new_pass = getpass("Enter your new password: ")
                if check_password(new_pass) is True:
                    new_pass = _generate_hash_pw(new_pass, "sha1")
                    sql_manager.change_pass(new_pass, logged_user)
                else:
                    print("Your new password sucks. Think of a better one!")
            else:
                print("The received code isn't valid.")

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == "show-balance":
            print("Current balance: ${}".format(logged_user.get_balance()))

        elif command == "withdraw":
            if sql_manager.are_available_tan_codes(username) is True:
                amount = float(input("amount: "))
                tan_code = input("TAN code: ")
                all_tan_codes = []
                for row in sql_manager.get_all_tan_codes(username):
                    all_tan_codes.append(row[0])
                print(all_tan_codes)
                if tan_code in all_tan_codes:
                    logged_user.withdraw(amount)
                    sql_manager.update_balance(logged_user.get_balance(), username)
                    sql_manager.delete_tan_code(username, tan_code)
                    print("Transaction successful.")
                else:
                    print("Invalid TAN Code.")
            else:
                print("You have 0 remaining TAN codes. Please generate more with <send-tan-codes>")

        elif command == "deposit":
            if sql_manager.are_available_tan_codes(username) is True:
                amount = float(input("amount: "))
                tan_code = input("TAN code: ")
                tan_code = _generate_hash_pw(tan_code, "sha224")
                if tan_code in sql_manager.get_all_tan_codes(username):
                    logged_user.deposit(amount)
                    sql_manager.update_balance(logged_user.get_balance(), username)
                    sql_manager.delete_tan_code(username, tan_code)
                    print("Transaction successful.")
                else:
                    print("Invalid TAN code.")
            else:
                print("You have 0 remaining TAN codes. Please generate more with <send-tan-codes>")

        elif command == "send-tan-codes":
            send_tan_codes(username)

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")
            print("show-balance - shows account's balance")
            print("withdraw - withdraws amount from account balance")
            print("deposit - deposits amount to account balance")
            print("send-tan-codes - sends TAN codes to the user email")
            print("exit - exits. Duh.")


# main
def main():
    sql_manager.create_clients_table()
    main_menu()


# PROGRAM RUN
if __name__ == '__main__':
    main()
