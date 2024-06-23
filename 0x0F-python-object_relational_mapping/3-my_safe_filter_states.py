#!/usr/bin/python3
""" This script takes in arguments and displays all values in the states."""
import MySQLdb
import sys

if __name__ == "__main__":
    un = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    db_conn = MySQLdb.connect(host="localhost", user=un, passwd=passw, db=db, port=3306)
    c = db_conn.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    c.execute(query, (state_name,))
    rs = c.fetchall()
    for r in rs:
        print(r)
    c.close()
    db_conn.close()
