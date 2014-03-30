# Interface for Problem X - Grocery store


# IMPORTS
from commandparser import CommandParser
from database import Database


class Store():
    """docstring for Command-line Interface"""
    def __init__(self, database_name):
        self.cp = CommandParser()
        self.db = Database(database_name)
        self._init_callbacks()
        self._loop()

    def callback_import_products_json(self, arguments):
        json_filename = " ".join(arguments)
        if self.db.import_products_json(json_filename) is True:
            return "{} imported.".format(json_filename[:-5])
        else:
            return "{} could not be imported.".format(json_filename)

    def callback_export_products_json(self, arguments):
        json_filename = " ".join(arguments)
        opened_file = open(json_filename, "w")
        opened_file.write(self.db.export_products_json())
        opened_file.close()
        return "Products exported to {}".format(json_filename)

    def callback_unknown_command(self, arguments):
        message = ("Error: Unknown Command!", "Why don't you enter help to see available commands?")
        return "\n".join(message)

    def callback_list_products(self, arguments):
        return self.db.list_products()

    def callback_add_product(self, arguments):
        name = str(input("name>"))
        price_per_kg = str(input("price per kg>"))
        quantity_in_kg = str(input("quantity in kg>"))
        if self.db.add_product(name, price_per_kg, quantity_in_kg):
            return "{} added to products.".format(name)

    def callback_delete_product(self, arguments):
        product_id = arguments[0]
        name = self.db.fetch_product_name(product_id)
        if self.db.delete_product(product_id) is True:
            return "{} deleted.".format(name)

    def callback_update_product(self, arguments):
        product_id = arguments[0]
        old_name = self.db.fetch_product_name(product_id)
        new_name = str(input("name>"))
        price_per_kg = str(input("price per kg>"))
        quantity_in_kg = str(input("quantity in kg>"))
        if self.db.update_product(new_name, price_per_kg, quantity_in_kg) is True:
            return "{} updated to {}.".format(old_name, new_name)

    def callback_import_customers_json(self, arguments):
        json_filename = " ".join(arguments)
        if self.db.import_customers_json(json_filename) is True:
            return "Imported customers from json_filename"

    def callback_list_customers(self, arguments):
        return self.db.list_customers()

    def callback_add_customer(self, arguments):
        name = input("name>")
        kg_bought = input("kg bought>")
        money_spent = input("money spent>")
        if self.db.add_customer(self, name, kg_bought, money_spent) is True:
            return "Added {}.".format(name)

    def callback_delete_customer(self, arguments):
        customer_id = arguments[0]
        if self.db.delete_customer(customer_id) is True:
            return "Deleted {}.".format(self.db.fetch_customer_name(customer_id))

    def callback_update_customer(self, arguments):
        customer_id = arguments[0]
        name = input("name>")
        kg_bought = input("kg bought>")
        money_spent = input("money spent>")
        if self.db.update_customer(self, name, kg_bought, money_spent, customer_id) is True:
            return "Updated {}".format(self.db)

    def callback_export_customers_json(self, arguments):
        json_filename = " ".join(arguments)
        opened_file = open(json_filename, "w")
        opened_file.write(self.db.export_customers_json())
        opened_file.close()
        return "Exported customers to {}".format(json_filename)

    def callback_help(self, arguments):
        help_message_products = ("* import_products_json <json_filename> - Adds products from the json file to the database.", "* list_products - Prints out all products in the following format: \"[id] name - price_per_kg BGN - quantity kg\"", "* add_product - Prompts for data, needed to add a new product to the database.", "* delete_product <product_id> - Removes the product matching the product id in the database.", "* update_product <product_id> - Updates the product data matching the product id in the database.", "* export_products_json <json_filename> - Exports the products to a json file.")
        help_message_customers = ("* import_json_customers <json_filename> - Adds customers from the json file to the database.", "* list_customers - Prints out all customers in the following format: \"[id] name - kg_bought kg - money_spent BGN\"", "* add_customer - Prompts for data, needed to add a new customer to the database.", "* delete_customer <customer_id> - Removes the customer matching the customer id in the database.", "* update_customer <customer_id> - Updates the customer data matching the customer id in the database.", "* export_customers_json <json_filename> - Exports the customers in the database to a json file.")
        return "\n".join(help_message_products + help_message_customers)


    def _init_callbacks(self):
        self.cp.on("list_products", self.callback_list_products)
        self.cp.on("list_customers", self.callback_list_customers)
        self.cp.on("add_product", self.callback_add_product)
        self.cp.on("add_customer", self.callback_add_customer)
        self.cp.on("update_product", self.callback_update_product)
        self.cp.on("update_customer", self.callback_update_customer)
        self.cp.on("delete_product", self.callback_delete_product)
        self.cp.on("delete_customer", self.callback_delete_customer)
        self.cp.on("import_products_json", self.callback_import_products_json)
        self.cp.on("import_customers_json", self.callback_import_customers_json)
        self.cp.on("export_products_json", self.callback_export_products_json)
        self.cp.on("export_customers_json", self.callback_export_customers_json)
        self.cp.on("help", self.callback_help)

    def _loop(self):
        while True:
            command = input(">")
            self.cp.take_command(command)
