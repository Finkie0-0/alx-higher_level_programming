#!/usr/bin/python3
""" a script that lists all states from the database """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                        user=sys.argv[1],
                        passwd=sys.argv[2],
                        db=sys.argv[3],
                        port=3306)
    """ Use a cursor object """
    cur = db.cursor()
    """ The function requires one parameter. """
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    """ Obtaining Query Results """
    rows = cur.fetchall()
    for row in rows:
        print(row)
    """ Close all cursors """
    cur.close()
    """ Close Databases """
    db.close()

