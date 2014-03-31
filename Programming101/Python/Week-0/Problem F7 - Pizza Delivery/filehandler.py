# Handles file-related tasks for attendance.py


# IMPORTS
from glob import glob
from time import time
from datetime import datetime
from collections import OrderedDict


class FileHandler():
    """docstring for FileHandler"""
    def __init__(self):
        self.history = []
        self.orders = OrderedDict()
        self.files = []

    def take_order(self, name, price):
        try:
            self.orders[name] += price
        except KeyError:
            self.orders[name] = price
        self.history.append("take")
        return True

    def list_orders(self):
        output = []
        for name in self.orders:
            output.append("{:<4} - {}".format(name, self.orders[name]))
        self.history.append("status")
        return "\n".join(output)

    def save_file(self):
        filename = "orders_{}".format(datetime.fromtimestamp(time()).strftime('%Y_%m_%d_%H_%M_%S'))
        opened_file = open(filename, "w")
        opened_file.write(self.list_orders())
        opened_file.close()
        self.history.append("save")
        return True

    def list_files(self):
        output = []
        self.files = self.fetch_files()
        for i, filename in enumerate(self.files):
            output.append("[{}] - {}".format(i+1, filename))
        self.history.append("list")
        return "\n".join(output)

    def fetch_files(self):
        return glob("orders_*")

    def fetch_file_name(self, list_id):
        return self.files[list_id]

    def load_file(self, list_id):
        if self.orders == {}:
            try:
                self.add_file_records_to_orders(list_id)
            except (IndexError, ValueError):
                return "Error: Invalid List ID."
            return True
        if self.files == []:
            return None
        elif self.history[-1] != "load":
            self.history.append("load")
            return False
        elif self.history[-1] == "load":
            try:
                self.add_file_records_to_orders(list_id)
            except (IndexError, ValueError):
                return "Error: Invalid List ID."
            return True

    def add_file_records_to_orders(self, list_id):
        self.orders.clear()
        opened_file = open(self.files[list_id], "r")
        contents = opened_file.readlines()
        opened_file.close()
        for line in contents:
            line = line.strip()
            line = line.split("-")
            print(line)
            self.take_order(line[0], int(line[1]))

    def fetch_history(self):
        return "\n".join(self.history)
