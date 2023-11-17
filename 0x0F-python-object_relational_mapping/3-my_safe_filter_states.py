#!/usr/bin/python3
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
    myCursor = dataBase.cursor()
    myCursor.execute("""SELECT * FROM states WHERE states.name IS '{}'
    ORDER BY ID ASC""".format(re.match("[A-Za-z\\s]+", sys.argv[4])[0]))
    result = myCursor.fetchall()
    for i in result:
        print(i)
    myCursor.close()
    dataBase.close()
