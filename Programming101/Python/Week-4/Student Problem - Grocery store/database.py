# Database for manage_store.py


# IMPORTS
import sqlite3
import json
from collections import OrderedDict


class Database():
    """docstring for Database"""
    def __init__(self, database_name):
        self.db = sqlite3.connect(database_name)
        self.cursor = self.db.cursor()

    def import_products_json(self, json_filename):
        try:
            opened_file = open(json_filename, "r")
        except IOError:
            return False
        json_contents = json.load(opened_file)
        for dictionary in json_contents:
            values = (dictionary["name"], dictionary["price_per_kg"], dictionary["quantity_in_kg"])
            self.cursor.execute("INSERT INTO products(name, price_per_kg, quantity_in_kg) VALUES(?, ?, ?);", (values))
        opened_file.close()
        self.db.commit()
        return True

    def export_products_json(self):
        database_contents = self.cursor.execute("SELECT name, price_per_kg, quantity_in_kg FROM products;")
        json_output = []
        for record in database_contents:
            json_dict = {}
            json_dict["name"] = record[0]
            json_dict["price_per_kg"] = record[1]
            json_dict["quantity_in_kg"] = record[2]
            json_output.append(json_dict)
        return json.dumps(json_output, indent=4, sort_keys=True)

    def list_products(self):
        output = []
        for product_id, name, price_per_kg, quantity_in_kg in self.cursor.execute("SELECT id, name, price_per_kg, quantity_in_kg FROM products;"):
            output.append("[{}] {} - {} BGN - {} kg".format(product_id, name, price_per_kg, quantity_in_kg))
        return "\n".join(output)

    def add_product(self, name, price_per_kg, quantity_in_kg):
        self.cursor.execute("INSERT INTO products(name, price_per_kg, quantity_in_kg) VALUES(?, ?, ?);", (name, price_per_kg, quantity_in_kg))
        self.db.commit()
        return True

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id=?;", (product_id,))
        self.db.commit()
        return True

    def update_product(self, new_name, price_per_kg, quantity_in_kg, product_id):
        self.cursor.execute("UPDATE products SET name=?, price_per_kg=?, quantity_in_kg=? WHERE id=?;", (new_name, price_per_kg, quantity_in_kg, product_id))
        return True

    def fetch_product_name(self, product_id):
        return self.cursor.execute("SELECT name FROM products WHERE id = ?;", (product_id,)).fetchone()[0]

    def fetch_customer_name(self, customer_id):
        return self.cursor.execute("SELECT name FROM customers WHERE id=?;", (customer_id,)).fetchone()[0]

    def import_customers_json(self, json_filename):
        try:
            opened_file = open(json_filename, "r")
        except IOError:
            return False
        json_contents = json.load(opened_file)
        for dictionary in json_contents:
            values = (dictionary["name"], dictionary["kg_bought"], dictionary["money_spent"])
            self.cursor.execute("INSERT INTO customers(name, kg_bought, money_spent) VALUES(?, ?, ?);", (values))
        opened_file.close()
        self.db.commit()
        return True

    def list_customers(self):
        output = []
        for customer_id, name, kg_bought, money_spent in self.cursor.execute("SELECT id, name, kg_bought, money_spent FROM customers;"):
            output.append("[{}] {} - {} kg - {} BGN".format(customer_id, name, kg_bought, money_spent))
        return "\n".join(output)

    def add_customer(self, name, kg_bought, money_spent):
        self.cursor.execute("INSERT INTO customers(name, kg_bought, money_spent) VALUES(?, ?, ?);", (name, kg_bought, money_spent))
        self.db.commit()
        return True

    def delete_customer(self, customer_id):
        self.cursor.execute("DELETE FROM customers WHERE id=?;", (customer_id,))
        self.db.commit()
        return True

    def update_customer(self, name, kg_bought, money_spent, customer_id):
        self.cursor.execute("UPDATE customers SET name=?, kg_bought=?, money_spent=? WHERE id=?", (name, kg_bought, money_spent, customer_id))
        return True

    def export_customers_json(self):
        database_contents = self.cursor.execute("SELECT name, kg_bought, money_spent FROM customers;")
        json_output = []
        for record in database_contents:
            json_dict = OrderedDict()
            json_dict["name"] = record[0]
            json_dict["kg_bought"] = record[1]
            json_dict["money_spent"] = record[2]
            json_output.append(json_dict)
        return json.dumps(json_output, indent=4)
