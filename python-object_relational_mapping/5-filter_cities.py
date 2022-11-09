#!/usr/bin/python3
"""script that takes in an argument and displays all values in the states"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities, states\
                WHERE states.id = cities.state_id AND states.name = %s\
                ORDER BY cities.id", (argv[4], ))
    rows = cur.fetchall()
    separator = ""
    for row in rows:
        print(separator, end="")
        print(row[0], end="")
        separator = ", "
    print("\n", end="")
    cur.close()
    db.close()
