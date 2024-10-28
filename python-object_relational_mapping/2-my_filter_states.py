#!/usr/bin/python3

"""
script que toma un argumento e imprime todos los valores
en la tabla de states donde nombre es equivalente a name
"""

import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    state = sys.argv[4]

    cur = db.cursor()
    cur.execute(f"SELECT * FROM states WHERE name = '{state}' ORDER BY id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
