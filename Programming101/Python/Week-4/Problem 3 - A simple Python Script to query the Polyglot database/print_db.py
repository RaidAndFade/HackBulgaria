# DOCUMENTATION


# IMPORTS
import sqlite3


def main():
    conn = sqlite3.connect("polyglot.db")
    cursor = conn.cursor()

    result = cursor.execute("SELECT id, name, monthly_salary, yearly_bonus, position FROM employees")

    for id, name, monthly_salary, yearly_bonus, position in result:
        print("-" * 90)
        print("Name: {}, Monthly salary: {}, Yearly Bonus: {}, Position: {}".format(name, monthly_salary, yearly_bonus, position))


# PROGRAM RUN
if __name__ == "__main__":
    main()
