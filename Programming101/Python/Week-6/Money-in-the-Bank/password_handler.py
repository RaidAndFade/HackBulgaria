# Handles password operations


# IMPORTS
from re import search
import hashlib
from string import punctuation


# FUNCTIONS
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


def _check_hash(received_code, true_code):
    return _generate_hash_pw(received_code, "sha224") == true_code
