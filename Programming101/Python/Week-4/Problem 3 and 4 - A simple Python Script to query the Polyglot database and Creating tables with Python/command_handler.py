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
        output = []
        for person_id, name, position in self.cursor.execute("SELECT id, name, position FROM employees;"):
            output.append("[{}] {} - {}".format(person_id, name, position))
        return "\n".join(output)

    def trigger_monthly_spending(self):
        return self.cursor.execute("SELECT SUM(monthly_salary) FROM employees;").fetchone()[0]

    def trigger_yearly_spending(self):
        return self.trigger_monthly_spending() * 12 + self.cursor.execute("SELECT SUM(yearly_bonus) FROM employees;").fetchone()[0]

    def trigger_add_employee(self):
        name = input("name>")
        monthly_salary = input("monthly_salary>")
        yearly_bonus = input("yearly_bonus>")
        position = input("position>")
        self.add_employee(name, monthly_salary, yearly_bonus, position)
        return "{} was added.".format(name)

    def add_employee(self, name, monthly_salary, yearly_bonus, position):
        try:
            sql_query = "INSERT INTO employees(name, monthly_salary, yearly_bonus, position) VALUES (?, ?, ?, ?);"
        except sqlite3.IntegrityError:
            return False
        self.cursor.execute(sql_query, (name, monthly_salary, yearly_bonus, position))
        self.conn.commit()
        return True

    def trigger_delete_employee(self, employee_id):
        try:
            name = self.cursor.execute("SELECT name FROM employees WHERE id=?;", (employee_id,)).fetchone()[0]
            self.cursor.execute("DELETE FROM employees WHERE id=?;", (employee_id,))
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            return False
        return "{} was deleted.".format(name)

    def trigger_update_employee(self, employee_id):
        name = str(input("name>"))
        monthly_salary = str(input("monthly_salary>"))
        yearly_bonus = str(input("yearly_bonus>"))
        position = str(input("position>"))
        sql_query = "UPDATE employees SET name=?, monthly_salary=?, yearly_bonus=?, position=?;"
        self.cursor.execute(sql_query, (name, monthly_salary, yearly_bonus, position))
        self.conn.commit()

    def trigger_help(self):
        help_message = ("list_employees - Prints out all employees, in the following format - \"name - position\"",
                        "monthly_spending - Prints out the total sum for monthly spending that the company is doing for salaries",
                        "yearly_spending - Prints out the total sum for one year of operation (Again, salaries)",
                        "add_employee, the program starts to promt for data, to create a new employee.",
                        "delete_employee <employee_id>, the program should delete the given employee from the database",
                        "update_employee <employee_id>, the program should prompt the user to change each of the fields for the given")
        return "\n".join(help_message)

    def trigger_unknown_command(self):
        unknown_command_mesage = ("Unknown command!", "Why don't you enter help to see the available commands?")
        return "\n".join(unknown_command_mesage)
