#!/usr/bin/python3
""" Write a script that lists all states in the database """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    """ Connects are made by creating a cursor object """
    cur = db.cursor()
    """ Execution requires a parameter """
    rows = cur.fetchall()
    for row in rows:
        print(row)
    """ close cursors """
    cur.close()
    """ close databases """
    db.close()

