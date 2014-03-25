# IMPORTS
import sqlite3


# FUNCTIONS
def create_tables(cursor):
    cursor.execute("CREATE TABLE employees(id INTEGER PRIMARY KEY ASC, name text, monthly_salary int, yearly_bonus int, position text)")


def get_file_contents(path):
    f = open(path, "r")
    contents = f.read()
    f.close()

    return contents


def insert(item, cursor):
    person_id = item["id"]
    name = item["name"]
    monthly_salary = item["monthly_salary"]
    yearly_bonus = item["yearly_bonus"]
    position = item["position"]

    query_lang = "INSERT INTO employees VALUES(?, ?, ?, ?, ?)"
    cursor.execute(
        query_lang, (person_id, name, monthly_salary, yearly_bonus, position))


data = [
    {
        "id": 1,
        "name": "Ivan Ivanov",
        "monthly_salary": 5000,
        "yearly_bonus": 10000,
        "position": "Software Developer"
    },
    {
        "id": 2,
        "name": "Rado Rado",
        "monthly_salary": 500,
        "yearly_bonus": 0,
        "position": "Technical Support Intern"
    },
    {
        "id": 3,
        "name": "Ivo Ivo",
        "monthly_salary": 10000,
        "yearly_bonus": 100000,
        "position": "CEO"
    },
    {
        "id": 4,
        "name": "Petar Petrov",
        "monthly_salary": 3000,
        "yearly_bonus": 1000,
        "position": "Marketing Manager",
    },
    {
        "id": 5,
        "name": "Maria Georgieva",
        "monthly_salary": 8000,
        "yearly_bonus": 10000,
        "position": "COO"
    }]


conn = sqlite3.connect("polyglot.db")
c = conn.cursor()

create_tables(c)

for item in data:
    insert(item, c)

conn.commit()
conn.close()
