#!/usr/bin/python3
'''lists all cities from the database hbtn_0e_0_usa'''
import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            password=argv[2],
            db=argv[3],
            port=3306
            )
    cur = conn.cursor()
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY id ASC
    """
    # cities.state_id is a foreign key in a cities table
    cur.execute(query)
    cities_list = cur.fetchall()
    for city in cities_list:
        print(city)
    cur.close()
    conn.close()
