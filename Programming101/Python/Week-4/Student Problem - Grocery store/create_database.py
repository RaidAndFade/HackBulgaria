# IMPORTS
import sqlite3


# FUNCTIONS
def create_table(cursor):
    cursor.execute("CREATE TABLE products(id INTEGER PRIMARY KEY ASC, name text, price_per_kg real, quantity_in_kg real)")
    cursor.execute("CREATE TABLE customers(id INTEGER PRIMARY KEY ASC, name text, kg_bought real, money_spent real)")


def create_database(database_name):
    db = sqlite3.connect(database_name)
    cursor = db.cursor()
    try:
        create_table(cursor)
    except sqlite3.OperationalError:
        print("Error: Table products already exists!")
        return 1
    db.commit()
    db.close()


# main
def main():
    database_name = str(input("Enter database name to create: "))
    create_database(database_name)


# PROGRAM RUN
if __name__ == '__main__':
    main()
