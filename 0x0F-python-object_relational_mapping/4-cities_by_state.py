#!/usr/bin/python3
""" This script lists all cities from the database. """
import MySQLdb
import sys

if __name__ == "__main__":
    un = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]

    db_conn = MySQLdb.connect(host="localhost", user=un, passwd=passw, db=db, port=3306)
    c = db_conn.cursor()
    c.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    rs = c.fetchall()
    for r in rs:
        print(r)
    c.close()
    db_conn.close()
