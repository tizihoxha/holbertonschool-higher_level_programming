#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0"""
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=argv1, passwd=argv2, db=argv3)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchcall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

