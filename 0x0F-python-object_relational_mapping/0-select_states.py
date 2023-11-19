#!/usr/bin/python3
"""
Displays Lista all states from hbtn_0e_0_usa DB.
"""
import MySQLdb
import sys
if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306)
        c = db.cursor()
        c.execute("SELECT * FROM states")
        r = c.fetchall()
        for ri in r:
            print(ri)
    except MySQLdb.Error as x:
        print("Error:", x)
    finally:
        if c:
            c.close()
        if db:
            db.close()
