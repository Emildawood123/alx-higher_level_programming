#!/usr/bin/python3
import sys
import MySQLdb
dataBase = MySQLdb.connect(
    user=sys.argv[1],
    passwd=sys.argv[2],
    host="localhost",
    port="3306",
    db=sys.argv[3]
)
myCursor = dataBase.cursor()
myCursor.execute("""SELECT * FROM states ORDER BY id ASC""")
result = myCursor.fetchall()
for i in result:
    print(i)
myCursor.close()
dataBase.close()
