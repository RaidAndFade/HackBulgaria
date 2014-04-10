# money-in-the-bank


## About:
The program is simulating common bank services with extra thoughts for security.


## The distinguishing features:
* The ``register`` forces you to use a secure password (more than 8 characters, must have a special symbol, uppercase and lowercase characters).


* All passwords are encrypted using SHA1 into a small database sqlite3.
There's the option to reset your password. You can send an email to the email associated with the username you're attempting to log in with.


* It's also secure (kind of, or maybe not really) against brute force attacks. After the 20th attempt to login, you'll
be denied access to that login and have to wait 5 minutes to attempt again. Unix timestamp is used to store time of
last failed login and current login attempt.


* You must generate [TAN codes](http://en.wikipedia.org/wiki/Transaction_authentication_number) to withdraw or deposit from/to bank accounts. TAN codes can be generated and sent to your email using ``send-tan-codes``.
They're random strings, hashed with sha22. Each transaction consumes 1 TAN code.

* **Note**: an user can have only 10 TAN codes. Deplete the 10 codes and then generate 10 new ones.


* Every password change confirmation code, reset password code and TAN code is hashed once more before being saved in the DB for extra security


## How to use:
Run with python3, start.py and use the ``help`` command. After registering and logging in, use the ``help`` command once more to see the new available commands.



**Note**: you need to provide a gmail username/password in a separate ``gmail_config.py`` file so you can send emails. Sorry, gmail limitations :(


## Dependencies:
* Python 3.x
* SQLite 3
