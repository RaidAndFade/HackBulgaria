# Database interface for mail.py


# IMPORTS
import sqlite3
import json


# FUNCTIONS
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


class DBInterface():
    """docstring for DBInterface"""
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.dict_cursor = self.conn.cursor()
        self.dict_cursor.row_factory = dict_factory

    def fetch_maillists(self):
        query = "SELECT id, name FROM maillists;"
        data = self.dict_cursor.execute(query).fetchall()
        return data

    def fetch_subscribers(self, unique_list_id):
        query = "SELECT maillists_to_subscribers.subscriber_id, subscribers.name, subscribers.email FROM maillists_to_subscribers INNER JOIN subscribers ON maillists_to_subscribers.subscriber_id = subscribers.id WHERE maillists_to_subscribers.maillist_id = ?;"
        data = self.dict_cursor.execute(query, (unique_list_id,)).fetchall()
        return data

    def fetch_maillist_name_by_id(self, maillist_id):
        query = "SELECT name FROM maillists WHERE id = ?;"
        data = self.dict_cursor.execute(query, (maillist_id,)).fetchone()
        return data

    def fetch_maillists_id_by_name(self, maillist_name):
        query = "SELECT id FROM maillists WHERE name = ?"
        data = self.dict_cursor.execute(query, (maillist_name,)).fetchone()
        return data

    def create_maillist(self, name):
        query = "SELECT id FROM maillists WHERE name = ?;"
        check = self.dict_cursor.execute(query, (name,)).fetchone()
        if check is not None:
            return False

        query = "INSERT INTO maillists VALUES(NULL, ?);"
        self.dict_cursor.execute(query, (name,))
        self.conn.commit()
        return True

    def update_maillist_name(self, maillist_id, new_name):
        query = "SELECT id FROM maillists WHERE name = ?;"
        check = self.dict_cursor.execute(query, (new_name,)).fetchone()
        if check is not None:
            return False
        query = "UPDATE maillists SET name = ? WHERE id = ?;"
        query_data = (new_name, maillist_id)
        self.dict_cursor.execute(query, query_data)
        self.conn.commit()
        return True

    def delete_maillist_by_id(self, maillist_id):
        query = "DELETE FROM maillists WHERE id = ?;"
        self.dict_cursor.execute(query, (maillist_id,))
        query = "DELETE FROM maillists_to_subscribers WHERE maillist_id = ?;"
        self.dict_cursor.execute(query, (maillist_id,))
        self.conn.commit()
        return True

    def add_subscriber(self, name, email, list_id):
        query = "SELECT id FROM subscribers WHERE email = ?;"
        check = self.dict_cursor.execute(query, (email,)).fetchone()
        if check is not None:
            return False
        data_to_insert = (name, email)
        self.dict_cursor.execute("INSERT INTO subscribers VALUES(NULL, ?, ?);", data_to_insert)

        subscriber_id = self.dict_cursor.execute(query, (email,)).fetchone()["id"]
        data_to_insert = (list_id, subscriber_id)
        query = "INSERT INTO maillists_to_subscribers VALUES(NULL, ?, ?);"
        self.dict_cursor.execute(query, data_to_insert)
        self.conn.commit()
        return True

    def update_subscriber(self, list_id, subscriber_id, updated_data):
        query = "UPDATE subscribers SET name = ?, email = ? WHERE id in (SELECT subscriber_id FROM maillists_to_subscribers WHERE maillist_id = ? and subscriber_id = ?);"
        data_tuple = (updated_data["name"], updated_data["email"], list_id, subscriber_id)
        self.dict_cursor.execute(query, data_tuple)
        self.conn.commit()
        return True

    def delete_subscriber(self, list_id, subscriber_id):
        query = "DELETE FROM maillists_to_subscribers WHERE maillist_id = ? and subscriber_id = ?;"
        self.dict_cursor.execute(query, (list_id, subscriber_id))
        self.conn.commit()
        return True

    def fetch_maillists_by_subscriber_email(self, email):
        # query = "SELECT maillists.name FROM maillists INNER JOIN maillists_to_subscribers ON maillists_to_subscribers.maillist_id = maillists.id INNER JOIN subscribers ON subscribers.id = maillists_to_subscribers.maillist_id WHERE subscribers.email = ?;"
        query = "SELECT maillists.id, maillists.name FROM maillists, subscribers WHERE subscribers.email = ?;"
        return self.dict_cursor.execute(query, (email,)).fetchall()

    def merge_lists(self, list_id_a, list_id_b, new_list_name):
        self.create_maillist(new_list_name)
        list_id = self.fetch_maillists_id_by_name(new_list_name)["id"]
        query = "SELECT subscriber_id FROM maillists_to_subscribers WHERE maillist_id = ? or maillist_id = ?;"
        subs_ids = self.dict_cursor.execute(query, (list_id_a, list_id_b)).fetchall()
        for sub in subs_ids:
            query = "INSERT INTO maillists_to_subscribers VALUES(NULL, ?, ?);"
            data = (list_id, sub["subscriber_id"])
            self.dict_cursor.execute(query, data)
        self.conn.commit()
        return True

    def export_json(self, list_id):
        query = "SELECT subscribers.id, subscribers.name, subscribers.email FROM subscribers INNER JOIN maillists_to_subscribers ON subscribers.id = maillists_to_subscribers.subscriber_id WHERE maillists_to_subscribers.maillist_id = ?;"
        data = self.dict_cursor.execute(query, (list_id,)).fetchall()
        return json.dumps(data, indent=4, sort_keys=True)
