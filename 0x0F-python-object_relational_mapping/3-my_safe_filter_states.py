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
    """
    query = "SELECT * FROM states WHERE name =
    {} ORDER BY id ASC".format(argv[4])
    Query at risk of sql injection
    Recommended - using a parameterized query with placeholders.
    """
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))
    """
    The comma after (state_name,)indicates that you are passing a
    tuple of a single element
    (the state_name value) to the execute() method.
    """
    states_list = cur.fetchall()
    for state in states_list:
        print(state)
    cur.close()
    conn.close()
