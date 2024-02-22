#!/usr/bin/python3
import MySQLdb
import sys

def get_all_states(username, password, dbname):
    """List all states from the database."""
    datab = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    c = datab.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    r = c.fetchall()
    for ir in r:
        print(ir)
    c.close()
    datab.close()


if __name__ == "__main__":
    get_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
