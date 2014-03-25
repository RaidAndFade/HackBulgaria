# Command_handler.py for manage_company.py


# IMPORTS
import sqlite3


class CommandHandler():
    """docstring for CommandHandler"""
    def __init__(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def parse_command(self, command):
        return tuple(command.split(" "))

    def is_command(self, command_tuple, command_string):
        return command_tuple[0] == command_string

    def trigger_list_employees(self):
        sql_query = "SELECT id, name, position FROM employees;"
        output = []
        for person_id, name, position in self.cursor.execute(sql_query):
            output.append("[{}] {} - {}".format(person_id, name, position))
        return "\n".join(output)

    def trigger_monthly_spending(self):
        sql_query = "SELECT monthly_salary FROM employees;"
        output_sum = 0
        for person_salary in self.cursor.execute(sql_query):
            output_sum += int(person_salary[0])
        return output_sum

    def trigger_yearly_spending(self):
        return self.trigger_monthly_spending() * 12

    def trigger_add_employee(self):
        name = str(input("name>"))
        monthly_salary = str(input("monthly_salary>"))
        yearly_bonus = str(input("yearly_bonus>"))
        position = str(input("position>"))
        sql_query = "INSERT INTO employees(name, monthly_salary, yearly_bonus, position) VALUES (?, ?, ?, ?)"
        self.cursor.execute(sql_query, (name, monthly_salary, yearly_bonus, position))
        self.conn.commit()

    def trigger_delete_employee(self, employee_id):
        sql_query = "SELECT name FROM employees WHERE id=?"
        name = self.cursor.execute(sql_query, employee_id).fetchone()
        sql_query = "DELETE FROM employees WHERE id=?"
        self.cursor.execute(sql_query, employee_id)
        self.conn.commit()
        return "{} was deleted.".format(name[0])

    def trigger_update_employee(self, employee_id):
        name = str(input("name>"))
        monthly_salary = str(input("monthly_salary>"))
        yearly_bonus = str(input("yearly_bonus>"))
        position = str(input("position>"))
        sql_query = "UPDATE employees SET name=?, monthly_salary=?, yearly_bonus=?, position=?;"
        self.cursor.execute(sql_query, (name, monthly_salary, yearly_bonus, position))
        self.conn.commit()

    def trigger_help(self):
        help_message = ["list_employees - Prints out all employees, in the following format - \"name - position\"",
                        "monthly_spending - Prints out the total sum for monthly spending that the company is doing for salaries",
                        "yearly_spending - Prints out the total sum for one year of operation (Again, salaries)",
                        "delete_employee <employee_id>, the program should delete the given employee from the database",
                        "update_employee <employee_id>, the program should prompt the user to change each of the fields for the given"]
        return "\n".join(help_message)

    def trigger_unknown_command(self):
        unknown_command_mesage = ["Unknown command!", "Why don't you enter help to see the available commands?"]
        return "\n".join(unknown_command_mesage)
