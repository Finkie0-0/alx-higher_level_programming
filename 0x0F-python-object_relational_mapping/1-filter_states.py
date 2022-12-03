#!/usr/bin/python3
""" Lists all states with a name starting with N from the data base htbn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    """ Put new connections"""
    cur = db.cursor()
    """ Requires one parameter to execute function"""
    cur.execute("SELECT * FROM states\
            WHERE name REGEXP BINARY\
            ORDER BY id ASC")
    """ Obtaining Query Results"""
    rows = cur.fetchall()
    for row in rows:
        print(row)
    """ Close cursor"""
    cur.close()
    """ close databases"""
    db.close()

