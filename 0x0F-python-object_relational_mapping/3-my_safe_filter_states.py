#!/usr/bin/python3
"""import libraries"""
import sys
import MySQLdb
import re
if __name__ == "__main__":
    dataBase = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    data = re.match("[A-Za-z\\s]+", sys.argv[4])
    command = """SELECT * FROM states WHERE BINARY name = '{}'
    ORDER BY ID ASC""".format(data[0])
    myCursor = dataBase.cursor()
    myCursor.execute(command)
    result = myCursor.fetchall()
    for i in result:
        print(i)
    myCursor.close()
    dataBase.close()
