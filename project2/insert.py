
import pymysql


# Establishing a connection to DB
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Ay032661308', db='users')
conn.autocommit(True)

# Getting a cursor from Database
cursor = conn.cursor()

# Inserting data into table
cursor.execute("INSERT into users.Players (name, id) VALUES ('john', 5)")

cursor.close()
conn.close()
