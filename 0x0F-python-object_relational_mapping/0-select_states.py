#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    datab = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = datab.cursor()
    c.execute("SELECT * FROM `states` ORDER BY `id` ASC")
    r = c.fetchall()
    for ir in r:
        print(ir)
    c.close()
    datab.close()
