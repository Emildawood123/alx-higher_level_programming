#!/usr/bin/python3
"""import libraries"""
import sys
import MySQLdb
if __name__ == "__main__":
    dataBase = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )
    myCursor = dataBase.cursor()
    myCursor.execute("""SELECT * FROM states ORDER BY ID ASC""")
    result = myCursor.fetchall()
    for i in result:
        print(i)
    myCursor.close()
    dataBase.close()
