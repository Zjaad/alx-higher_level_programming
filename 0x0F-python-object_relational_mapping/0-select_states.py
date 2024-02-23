#!/usr/bin/python3
import sys
import MySQLdb

def safe_filter_states(username, password, dbname, state_name):
    """Safely display all states matching the user-provided name."""
    datab = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    c = datab.cursor()
    c.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))
    r = c.fetchall()
    for ir in r:
        print(ir)
    c.close()
    datab.close()

if __name__ == "__main__":
    safe_filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
