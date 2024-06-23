#!/usr/bin/python3
import MySQLdb
import sys
""" lists all states with a name starting with N.  """
if __name__ == "__main__":
    un = sys.argv[1]
    passw = sys.argv[2]
    db = sys.argv[3]
    db_conn = MySQLdb.connect(host="localhost", user=un, passwd=passw, db=db, port=3306)
    c = db_conn.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    rs = c.fetchall()
    
    for r in rs:
        print(r)

    c.close()
    db_conn.close()
