import pymysql

conn = pymysql.connect(host='remotemysql.com', port=3306, user='isnXgmYxGG', passwd='zew8EOskBp', db='isnXgmYxGG')
conn.autocommit(True)

cursor = conn.cursor()

# 2
# cursor.execute("INSERT into isnXgmYxGG.dogs (name, age, breed) VALUES ('bono', 11, 'pointer')")
# cursor.execute("INSERT into isnXgmYxGG.dogs (name, age, breed) VALUES ('sheleg', 9, 'wolf')")
# cursor.execute("INSERT into isnXgmYxGG.dogs (name, age, breed) VALUES ('lili', 7, 'vizsla')")
#
# # 3
# cursor.execute("UPDATE isnXgmYxGG.dogs SET age = '10' WHERE name = 'bono'")
# #
# # 4
# cursor.execute("DELETE FROM isnXgmYxGG.dogs WHERE breed = 'vizsla'")

# # 5
# cursor.execute("SELECT name FROM isnXgmYxGG.dogs;")
# for row in cursor:
#     print(row)

cursor.close()
conn.close()

