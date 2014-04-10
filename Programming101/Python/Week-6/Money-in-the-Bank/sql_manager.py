import sqlite3
from Client import Client
from time import time

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''CREATE TABLE IF NOT EXISTS
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                email TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                attempts INTEGER DEFAULT 0,
                time INTEGER DEFAULT 0,
                UNIQUE (username));'''
    cursor.execute(create_query)
    create_query = '''CREATE TABLE IF NOT EXISTS
        resetcodes(username TEXT PRIMARY KEY,
                    code TEXT);'''
    cursor.execute(create_query)
    create_query = '''CREATE TABLE IF NOT EXISTS
        tancodes(username TEXT,
                    code TEXT);'''
    cursor.execute(create_query)


def add_tan_code(username, tan_code):
    cursor.execute("INSERT INTO tancodes VALUES(?, ?);", (username, tan_code))
    conn.commit()


def delete_tan_code(username, tan_code):
    cursor.execute("DELETE FROM tancodes WHERE username = ? and code = ?;", (username, tan_code))
    conn.commit()


def delete_tan_codes(username):
    cursor.execute("DELETE FROM tancodes WHERE username = ?;", (username,))
    conn.commit()


def get_tan_code(username):
    return cursor.execute("SELECT code FROM tancodes WHERE username = ?;", (username,)).fetchone()[0]


def add_reset_code(username, reset_code):
    cursor.execute("INSERT OR REPLACE INTO resetcodes VALUES(?, ?);", (username, reset_code))
    conn.commit()


def are_available_tan_codes(username):
    if cursor.execute("SELECT Count(*) FROM tancodes WHERE username = ?;", (username,)).fetchone()[0] > 0:
        return True
    return False


def get_all_tan_codes(username):
    codes = cursor.execute("SELECT code FROM tancodes WHERE username = ?;", (username,)).fetchall()
    output = []
    for row in codes:
        output.append(row[0])
    return output


def get_reset_code(username):
    return cursor.execute("SELECT code FROM resetcodes WHERE username = ?;", (username,)).fetchone()[0]


def failed_login(username):
    timestamp = int(time())
    attempts = cursor.execute("SELECT attempts FROM clients WHERE username = ?;", (username,)).fetchone()[0] + 1
    query = "UPDATE clients SET attempts = ?, time = ? WHERE username = ?;"
    cursor.execute(query, (attempts, timestamp, username))
    conn.commit()


def reset_failed_login(username):
    cursor.execute("UPDATE clients SET attempts = 0, time = 0 WHERE username = ?;", (username,))
    conn.commit()


def reset_failed_logins():
    cursor.execute("UPDATE clients SET attempts = 0, time = 0;")
    conn.commit()


def get_current_time(username):
    return cursor.execute("SELECT time FROM clients WHERE username = ?;", (username,)).fetchone()[0]


def get_attempts(username):
    return cursor.execute("SELECT attempts FROM clients WHERE username = ?;", (username,)).fetchone()[0]


def get_email(username):
    return cursor.execute("SELECT email FROM clients WHERE username = ?;", (username,)).fetchone()[0]


def update_balance(new_balance, username):
    cursor.execute("UPDATE clients SET balance = ? WHERE username = ?", (new_balance, username))
    conn.commit()


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?;"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?;"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def change_pass_by_username(username, new_password):
    cursor.execute("UPDATE clients SET password = ? WHERE username = ?;", (new_password, username))
    conn.commit()


def register(username, password, email):
    insert_sql = "INSERT INTO clients (username, password, email) VALUES (?, ?, ?);"
    cursor.execute(insert_sql, (username, password, email))
    conn.commit()


def login(username, password):
    select_query = "SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1;"
    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()
    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
