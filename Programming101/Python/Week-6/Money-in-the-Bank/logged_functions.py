# Functions available for logged in users


# IMPORTS
from getpass import getpass
import sql_manager
import password_handler
import smtp_handler


# FUNCTIONS
def info(logged_user):
    print("You are: " + logged_user.get_username())
    print("Your id is: " + str(logged_user.get_id()))
    print("Your balance is:" + str(logged_user.get_balance()) + '$')


def change_pass(logged_user):
    smtp_handler.send_reset_code(logged_user.get_username())
    received_code = input("The code you received: ")
    if sql_manager.get_reset_code(logged_user.get_username()) == received_code:
        new_pass = getpass("Enter your new password: ")
        if password_handler.check_password(new_pass) is True:
            new_pass = password_handler._generate_hash_pw(new_pass, "sha1")
            sql_manager.change_pass(new_pass, logged_user)
        else:
            print("Your new password sucks. Think of a better one!")
    else:
        print("The entered code isn't valid.")


def change_message(logged_user):
    new_message = input("Enter your new message: ")
    sql_manager.change_message(new_message, logged_user)
    print("Message chnaged!")


def withdraw(logged_user):
    if sql_manager.are_available_tan_codes(logged_user.get_username()) is True:
        amount = float(input("amount: "))
        tan_code = input("TAN code: ")
        all_tan_codes = []
        for row in sql_manager.get_all_tan_codes(logged_user.get_username()):
            all_tan_codes.append(row[0])
        print(all_tan_codes)
        if tan_code in all_tan_codes:
            logged_user.withdraw(amount)
            sql_manager.update_balance(logged_user.get_balance(), logged_user.get_username())
            sql_manager.delete_tan_code(logged_user.get_username(), tan_code)
            print("Transaction successful.")
        else:
            print("Invalid TAN Code.")
    else:
        print("You have 0 remaining TAN codes. Please generate more with <send-tan-codes>")


def deposit(logged_user):
    if sql_manager.are_available_tan_codes(logged_user.get_username()) is True:
        amount = float(input("amount: "))
        tan_code = input("TAN code: ")
        tan_code = password_handler._generate_hash_pw(tan_code, "sha224")
        if tan_code in sql_manager.get_all_tan_codes(logged_user.get_username()):
            logged_user.deposit(amount)
            sql_manager.update_balance(logged_user.get_balance(), logged_user.get_username())
            sql_manager.delete_tan_code(logged_user.get_username(), tan_code)
            print("Transaction successful.")
        else:
            print("Invalid TAN code.")
    else:
        print("You have 0 remaining TAN codes. Please generate more with <send-tan-codes>")


def send_tan_codes(logged_user):
    if smtp_handler.send_tan_codes(logged_user.get_username()) is True:
        print("Sent 10 TAN codes!")


def help():
    print("info - show account info")
    print("changepass - change password")
    print("change-message - change user message")
    print("show-message - show user's message")
    print("show-balance - show account balance")
    print("withdraw - withdraws amount from account balance")
    print("deposit - deposits amount to account balance")
    print("send-tan-codes - sends TAN codes to the user email")
    print("logout - Logouts from current user.")
