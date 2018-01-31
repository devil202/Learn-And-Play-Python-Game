import sqlite3
import string
conn=sqlite3.connect('C:\\Users\\DEV!L\\Documents\\python\game1.db')
c=conn.cursor()
a=" "
print c.execute("delete from user where 1=1")
conn.commit()
p=c.fetchall()
print p
conn.close()
