import pymysql

# Establishing a connection to DB
conn = pymysql.connect(host='remotemysql.com', port=3306, user='isnXgmYxGG', passwd='zew8EOskBp', db='isnXgmYxGG')
#conn.autocommit(True)

# Getting a cursor from Database
#cursor = conn.cursor()

# Getting all data from table “players”
#cursor.execute("SELECT * FROM users.Players;")

# Iterating table and printing all users
#for row in cursor:
#    print(row)

#cursor.close()
conn.close()



#
# You have successfully created a new database. The details are below.
#
# Username: isnXgmYxGG
#
# Database name: isnXgmYxGG
#
# Password: zew8EOskBp
#
# Server: remotemysql.com
#
# Port: 3306
#
# These are the username and password to log in to your database and phpMyAdmin




