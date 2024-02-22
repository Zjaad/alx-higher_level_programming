#!/usr/bin/python3
import MySQLdb
import sys


def filter_states_by_user_input(username, password, dbname, state_name):
    """ Display all states matching the user-provided name. """
    datab = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=dbname)
    c = datab.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    c.execute(query)
    r = c.fetchall()
    for ir in r:
        print(ir)
    c.close()
    datab.close()


if __name__ == "__main__":
    filter_states_by_user_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
