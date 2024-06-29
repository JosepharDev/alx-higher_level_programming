#!/usr/bin/python3
""" lists all cities of that state,
    using the database hbtn_0e_4_usa """

import sys
import MySQLdb


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    mysql_database = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_database
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """, (state_name, ))
    print(", ".join(map(lambda x: x[0], cur.fetchall())))
    cur.close()
    conn.close()
