#!/usr/bin/python3
"""Displays lists all states from hbtn_0e_0_usa DB."""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                .format(sys.argv[4]))
    r = c.fetchall()
    for ri in r:
        print(ri)
    c.close()
    db.close()
