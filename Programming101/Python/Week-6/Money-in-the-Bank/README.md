money-in-the-bank
=================

## About:
The program is simulating common bank services.

# The distinguishing features:
The register forces you to use a secure password (more than 8 characters, must have a special symbol, uppercase and lowercase characters).
All passwords are encrypted using SHA1 into a small database sqlite3.
There's the option to reset your password. You can send an email to the email associated with the username you're attempting to log in with.
It's also secure (kind of, or maybe not really) against brute force attacks. After the 20th attempt to login, you'll
be denied access to that login and have to wait 5 minutes to attempt again. Unix timestamp is used to store time of
last failed login and current login attempt.


## How to use:
Run with python3, start.py and use the ``help`` command.

## Dependancies:
Python3
sqlite3
