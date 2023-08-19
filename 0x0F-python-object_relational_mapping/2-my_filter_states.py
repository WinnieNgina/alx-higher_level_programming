#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    state_name = argv[4]
    conn = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            password=argv[2],
            db=argv[3],
            port=3306
            )
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
# Query at risk of sql injection
    cur.execute(query)
    states_list = cur.fetchall()
    for state in states_list:
        print(state)
    cur.close()
    conn.close()
