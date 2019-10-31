import sqlite3

aggregations = {1 : "avg",
                2 : "max",
                3 : "min",
                4 : "sum"}

def compute_aggregation(operation):

    query = f"SELECT {aggregations[operation]}(number) FROM numbers"

    with sqlite3.connect("newnum.db") as connection:
        c = connection.cursor()

        c.execute(query)

        result = c.fetchone()

        print(f"{operation} : {result[0]}")

prompt = """
Select the operation that you want to perform [1-5]:
1. Average
2. Max
3. Min
4. Sum
5. Exit
"""

user_input = input(prompt).strip()
valid_input = ("1", "2", "3", "4", "5")

while user_input not in valid_input:
    user_input = input("Enter a valid operation to perform [1-5]: ").strip()

user_input = int(user_input)

if user_input in (1, 2, 3, 4):
    compute_aggregation(user_input)
else:
    print("Exit")