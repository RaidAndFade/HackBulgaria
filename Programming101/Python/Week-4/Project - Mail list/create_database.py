# Creates a database for mail.py or creates a test database for unit tests


# IMPORTS
import sqlite3


# FUNCTIONS
def create_tables(cursor):
    cursor.execute("""CREATE TABLE maillists
                    (id INTEGER PRIMARY KEY, name text);""")
    cursor.execute("""CREATE TABLE subscribers
                    (id INTEGER PRIMARY KEY, name text, email text);""")
    cursor.execute("""CREATE TABLE maillists_to_subscribers
                    (id INTEGER PRIMARY KEY, maillist_id int, subscriber_id int,
                        FOREIGN KEY(maillist_id) REFERENCES maillists(id),
                        FOREIGN KEY(subscriber_id) REFERENCES subscribers(id));""")


def insert_maillist(item, cursor):
    name = item["name"]
    data_to_insert = (name,)

    query = "INSERT INTO maillists VALUES(NULL, ?)"
    cursor.execute(query, data_to_insert)


def insert_subscriber(item, cursor):
    name = item["name"]
    email = item["email"]
    data_to_insert = (name, email)

    query = "INSERT INTO subscribers VALUES(NULL, ?, ?)"
    cursor.execute(query, data_to_insert)


def insert_maillist_to_subscriber(item, cursor):
    maillist_id = item["maillist_id"]
    subscriber_id = item["subscriber_id"]
    data_to_insert = (maillist_id, subscriber_id)

    query = "INSERT INTO maillists_to_subscribers VALUES(NULL, ?, ?)"
    cursor.execute(query, data_to_insert)


def create_database(database_name, fake):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    try:
        create_tables(cursor)
    except sqlite3.OperationalError:
        return "Error: Database already exists"

    if fake.lower() == "y":
        maillists = [{
            "name": "Hack Bulgaria"
        }, {
            "name": "HackFMI"
        }]

        subscribers = [{
            "name": "RadoRado",
            "email": "radorado@hackbulgaria.com"
        }, {
            "name": "IvoIvo",
            "email": "ivo@hackbulgaria.com"
        }, {
            "name": "Tedi",
            "email": "tedi@hackbulgaria.com"
        }, {
            "name": "Anto",
            "email": "syndbg@hackbulgaria.com"
        }]

        maillists_to_subscribers = [{
            "maillist_id": 1,
            "subscriber_id": 1
        }, {
            "maillist_id": 1,
            "subscriber_id": 2
        }, {
            "maillist_id": 2,
            "subscriber_id": 2
        }, {
            "maillist_id": 2,
            "subscriber_id": 3
        }, {
            "maillist_id": 2,
            "subscriber_id": 4
        }]
        for item in maillists:
            insert_maillist(item, cursor)

        for item in subscribers:
            insert_subscriber(item, cursor)

        for item in maillists_to_subscribers:
            insert_maillist_to_subscriber(item, cursor)
    conn.commit()
    conn.close()


# main
def main():
    database_name = str(input("database name>"))
    fake = str(input("fake records(Y/N)>"))
    create_database(database_name, fake)


# PROGRAM RUN
if __name__ == '__main__':
    main()
