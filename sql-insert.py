import sqlite3
import random

numbers = []

for n in range(100):
    numbers.append((random.randint(0, 100),))

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    try:
        c.execute("CREATE TABLE numbers (number INT)")
        c.executemany("INSERT INTO numbers(number) values(?)", numbers)
    except sqlite3.OperationalError:
        print("Oops! Something went wrong. Try again...")