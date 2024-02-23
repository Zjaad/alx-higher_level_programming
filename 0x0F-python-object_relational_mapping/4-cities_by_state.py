#!/usr/bin/python3
"""Displays lists all states from DB."""
import MySQLdb
import sys

if __name__ == "__main__":
    datab = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    c = datab.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id""")
    r = c.fetchall()

    for ri in r:
        print(ri)
    c.close()
    datab.close()
