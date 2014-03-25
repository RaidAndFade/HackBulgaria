# IMPORTS
import sqlite3


# FUNCTIONS
def create_tables(cursor):
    cursor.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY ASC, name text, monthly_salary int, yearly_bonus int, position text)")


def insert(item, cursor):
    name = item["name"]
    monthly_salary = item["monthly_salary"]
    yearly_bonus = item["yearly_bonus"]
    position = item["position"]

    query_lang = "INSERT INTO employees VALUES(NULL, ?, ?, ?, ?)"
    cursor.execute(
        query_lang, (name, monthly_salary, yearly_bonus, position))


def create_database(database_name):
    data = [
        {
            "name": "Ivan Ivanov",
            "monthly_salary": 5000,
            "yearly_bonus": 10000,
            "position": "Software Developer"
        },
        {
            "name": "Rado Rado",
            "monthly_salary": 500,
            "yearly_bonus": 0,
            "position": "Technical Support Intern"
        },
        {
            "name": "Ivo Ivo",
            "monthly_salary": 10000,
            "yearly_bonus": 100000,
            "position": "CEO"
        },
        {
            "name": "Petar Petrov",
            "monthly_salary": 3000,
            "yearly_bonus": 1000,
            "position": "Marketing Manager",
        },
        {
            "name": "Maria Georgieva",
            "monthly_salary": 8000,
            "yearly_bonus": 10000,
            "position": "COO"
        }]

    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    try:
        create_tables(c)
    except Exception:
        print("Error:Table employees already exists!")
        return 1

    for item in data:
        insert(item, c)

    conn.commit()
    conn.close()


def main():
    database_name = str(input("Enter database name to create: "))
    create_database(database_name)


if __name__ == '__main__':
    main()
