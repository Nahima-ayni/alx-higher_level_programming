#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(
            user=argv[1], password=argv[2], database=argv[3], host="localhost", port=3306)

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY cities.id ASC")

    result = cursor.fetchall()
    for x in result:
        print(x)
