# import from csv

# import the csv library
import csv

import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    employees = csv.reader(open("employees.csv", "r", newline=None))

    # create a new table called employees
    c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

    # insert data into table
    c.executemany("INSERT INTO employees(firstname, lastname) values \
        (?, ?)", employees)