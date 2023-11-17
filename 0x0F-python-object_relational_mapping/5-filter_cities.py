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
    command = """SELECT cities.name
    FROM cities INNER JOIN states ON
    cities.state_id = states.id
    WHERE BINARY states.name = '{}'
    ORDER BY cities.id ASC""".format(sys.argv[4])
    myCursor.execute(command)
    result = myCursor.fetchall()
    if (len(result) == 0):
        print()
    else:
        for i in result:
            print("{}, ".format(i), end='')
        print(result[-1][0])
    myCursor.close()
    dataBase.close()
