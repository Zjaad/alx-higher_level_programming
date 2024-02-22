#!/usr/bin/python3
import MySQLdb
import sys

def filter_states(username, password, dbname):
    """List all states with a name starting with 'N'."""
    datab = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    c = datab.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    r = c.fetchall()
    for ir in r:
        print(ir)
    c.close()
    datab.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
