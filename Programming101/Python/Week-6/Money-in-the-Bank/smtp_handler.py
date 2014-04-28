# Handles SMTP operations


# IMPORTS
import sql_manager
import password_handler
from random_password_generator import generatePassword
from smtplib import SMTP
import gmail_config


# FUNCTIONS
def send_email(username, gmail_email, text, body):
    smtp_server = establish_connection(username)
    try:
        smtp_server.sendmail(
            "money-in-the-bank@awesome-app.com", gmail_email, body)
        print('Email sent.')
    except Exception as e:
        print(e)
        print('Error sending mail.')
        return False
    smtp_server.quit()
    return True


def establish_connection(username):
    gmail_username = gmail_config.get_username()
    gmail_password = gmail_config.get_password()
    smtp_server = SMTP("smtp.gmail.com", 587)
    smtp_server.ehlo()
    smtp_server.starttls()
    smtp_server.login(gmail_username, gmail_password)
    return smtp_server


def send_reset_code(username):
    gmail_email = sql_manager.get_email(username)
    reset_code = password_handler._generate_hash_pw(
        generatePassword(10), "sha1")
    TEXT = "Reset/confirmation code <{}>.".format(reset_code)
    BODY = '\r\n'.join(['To: {}'.format(gmail_email),
                        'From: money-in-the-bank@awesome-app.com',
                        'Subject: Your reset/confirmation code for username {}'.format(username), '', TEXT])
    if send_email(username, gmail_email, TEXT, BODY) is True:
        reset_code = password_handler._generate_hash_pw(reset_code, "sha224")
        sql_manager.add_reset_code(username, reset_code)
        return True
    return False


def send_tan_codes(username):
    if sql_manager.are_available_tan_codes(username) is True:
        print("You have available TAN codes. Use them before you generate new ones.")
        return
    tan_codes = []
    for i in range(10):
        tan_code = password_handler._generate_hash_pw(generatePassword(10), "sha224")
        tan_codes.append(tan_code)
    TEXT = "TAN CODES: {}.".format("\n".join(tan_codes))
    gmail_email = sql_manager.get_email(username)
    BODY = '\r\n'.join(['To: {}'.format(gmail_email),
                        'From: money-in-the-bank@awesome-app.com',
                        'Subject: Your TAN code for username {}'.format(username), '', TEXT])
    if send_email(username, gmail_email, TEXT, BODY) is True:
        sql_manager.delete_tan_codes(username)
        for tan_code in tan_codes:
            tan_code = password_handler._generate_hash_pw(tan_code, "sha224")
            sql_manager.add_tan_code(username, tan_code)
        return True
