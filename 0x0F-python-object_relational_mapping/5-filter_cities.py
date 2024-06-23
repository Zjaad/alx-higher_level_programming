#!/usr/bin/python3
"""
it takes in the name of a state as an argument and lists all cities of that state,
using the database."""

import MySQLdb
import sys

if __name__ == "__main__":
    un = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    db_conn = MySQLdb.connect(host="localhost", user=un, passwd=passw, db=db, port=3306)
    c = db_conn.cursor()
    query = ("SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    c.execute(query, (state_name,))
    rs = c.fetchall()
    city_names = [r[0] for r in rs]
    print(", ".join(city_names))
    c.close()
    db_conn.close()
