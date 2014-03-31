# IMPORTS
from commandparser import CommandParser
from sys import exit
import db_interface


class MailListProgram():
    """docstring for MailListProgram"""
    def __init__(self):
        self.cp = CommandParser()
        self.db = db_interface.DBInterface("mail_lists.db")
        self._init_callbacks()
        self._loop()

    def create_list_callback(self, arguments):
        name = " ".join(arguments)s
        if self.db.create_maillist(name) is True:
            return "<{}> was created.".format(name)
        else:
            return "<{}> failed to create.".format(name)

    def add_subscriber_callback(self, arguments):
        list_id = arguments[0]
        name = input("name>")
        email = input("email>")

        if self.db.add_subscriber(name, email, list_id) is True:
            list_name = self.db.fetch_maillist_name_by_id(list_id)["name"]
            return "{} added to list {}".format(name, list_name)
        else:
            return "Failed to add <{}> to list <{}>."

    def show_lists_callback(self, arguments):
        output_message = []
        for dictionary in self.db.fetch_maillists():
            string = "[{}] <{}>".format(dictionary["id"], dictionary["name"])
            output_message.append(string)
        return "\n".join(output_message)

    def show_list_callback(self, arguments):
        try:
            list_id = int("".join(arguments))
        except ValueError:
            return "Error: Invalid list id."
        output_message = []
        try:
            subscribers = self.db.fetch_subscribers(list_id)
            list_name = self.db.fetch_maillist_name_by_id(list_id)["name"]
            output_message.append("~~~~~~~<{}>~~~~~~~".format(list_name))
            for line in subscribers:
                output_message.append("[{}] <{}> - <{}>".format(line["subscriber_id"], line["name"], line["email"]))
        except TypeError:
            output_message.append("List with id <{}> was not found.".format(list_id))
        return "\n".join(output_message)

    def delete_mail_list_callback(self, arguments):
        maillist_id = " ".join(arguments)
        self.db.delete_maillist_by_id(maillist_id)
        return "Mail list with id {} was deleted.".format(maillist_id)

    def update_mail_list_name_callback(self, arguments):
        maillist_id = arguments[0]
        arguments.remove(maillist_id)
        new_name = " ".join(arguments)
        if self.db.update_maillist_name(maillist_id, new_name) is True:
            return "Mail list with id {} updated to <{}>.".format(maillist_id, new_name)
        else:
            return "Mail list with id {} not found.".format(maillist_id)

    def update_subscriber_callback(self, arguments):
        list_id = arguments[0]
        subscriber_id = arguments[1]
        name = str(input("name>"))
        email = str(input("email>"))
        data = {}
        data["name"] = name
        data["email"] = email
        self.db.update_subscriber(list_id, subscriber_id, data)
        return "Updated <{}>.".format(data["name"])

    def remove_subscriber_callback(self, arguments):
        list_id = arguments[0]
        subscriber_id = arguments[1]
        if self.db.delete_subscriber(list_id, subscriber_id) is True:
            return "{} deleted from {}".format()

    def search_email_callback(self, arguments):
        email = arguments[0]
        found_in_lists = self.db.fetch_maillists_by_subscriber_email(email)
        output_message = []
        for a_list in found_in_lists:
            output_message.append("[{}] {}".format(a_list["id"], a_list["name"]))
        return "\n".join(output_message)

    def merge_lists_callback(self, arguments):
        list_id_a = arguments[0]
        list_id_b = arguments[1]
        arguments.remove(list_id_a)
        arguments.remove(list_id_b)
        new_list_name = " ".join(arguments)
        self.db.merge_lists(list_id_a, list_id_b, new_list_name)
        return "Merged lists with ids {} and {} to <{}>".format(list_id_a, list_id_b,new_list_name)

    def export_json_callback(self, arguments):
        list_id = arguments[0]
        json_contents = self.db.export_json(list_id)
        list_name = self.db.fetch_maillist_name_by_id(list_id)["name"].replace(" ", "_")
        file_name = "{}.json".format(list_name)
        opened_file = open(file_name, "w")
        opened_file.write(json_contents)
        opened_file.close()
        return "{} exported to {}".format(list_name, file_name)

    def help_callback(self, arguments):
        output_message = ("Here is a full list of commands:",
                        "* show_lists - Prints all lists to the screen. Each list is assigned with a unique identifier",
                        "* show_list <unique_list_identifier> - Prints all people, one person at a line, that are subscribed for the list. The format is: <Name> - <Email>",
                        "* add <unique_list_identifier> - Starts the procedure for adding a person to a mail list. The program prompts for name and email.",
                        "* update_subscriber <unique_list_identifier> <unique_name_identifier> - updates the information for the given subscriber in the given list",
                        "* remove_subscriber <unique_list_identifier> <unique_name_identifier> - Removes the given subscriber from the given list",
                        "* create <list_name> - Creates a new empty list, with the given name.",
                        "* update <unique_list_identifier>  <new_list_name> - Updates the given list with a new name.",
                        "* delete <unique_list_identifier> - Deletes the given list from the database.",
                        "* search_email <email> - Performs a search into all lists to see if the given email is present. Shows all lists, where the email was found.",
                        "* merge_lists <list_identifier_1> <list_identifier_2> <new_list_name> - merges list1 and list2 into a new list, with the given name.",
                        "* export <unique_list_identifier> - Exports the given list into JSON file, named just like the list. All white spaces are replaced by underscores.",
                        "* exit - this will quit the program")
        return "\n".join(output_message)

    def exit_callback(self, arguments):
        exit(0)

    def _init_callbacks(self):
        self.cp.on("show_lists", self.show_lists_callback)
        self.cp.on("show_list", self.show_list_callback)
        self.cp.on("add", self.add_subscriber_callback)
        self.cp.on("update_subscriber", self.update_subscriber_callback)
        self.cp.on("remove_subscriber", self.remove_subscriber_callback)
        self.cp.on("delete", self.delete_mail_list_callback)
        self.cp.on("create", self.create_list_callback)
        self.cp.on("update", self.update_mail_list_name_callback)
        self.cp.on("search_email", self.search_email_callback)
        self.cp.on("merge_lists", self.merge_lists_callback)
        self.cp.on("export_json", self.export_json_callback)
        self.cp.on("exit", self.exit_callback)
        self.cp.on("help", self.help_callback)

    def _loop(self):
        while True:
            command = input(">")
            self.cp.take_command(command)


# PROGRAM RUN
if __name__ == '__main__':
    MailListProgram()
