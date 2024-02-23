#!/usr/bin/python3
"""Displays lists all cities from a given state in the DB."""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, state_name = sys.argv[1:5]

    datab = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)

    c = datab.cursor()
    c.execute("SELECT cities.name FROM cities "
              "JOIN states ON states.id = cities.state_id "
              "WHERE states.name = %s", (state_name,))

    cities = [row[0] for row in c.fetchall()]
    print(*cities, sep=", ")

    c.close()
    datab.close()
