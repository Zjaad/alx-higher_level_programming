#!/usr/bin/python3
"""
Displays all states with name starting with 'N' from the DB.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        datab = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3], port=3306)
        c = datab.cursor()
        c.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
        r = c.fetchall()
        for ri in r:
            print(ri)
    except MySQLdb.Error as w:
        print("Error:", w)

    finally:
        if c:
            c.close()
        if datab:
            datab.close()
