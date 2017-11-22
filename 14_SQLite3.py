# this script creates a SQLite DB with sqlite3 module in Python
# as sqlite3 is a default Python module no installation is needed
import sqlite3
# delete the raspi.db if it exists
conn=sqlite3.connect('raspi.db') # create and connet to a new DB
cursor=conn.cursor() # point to the new DB
# insert some data
cursor.execute('''
    CREATE TABLE users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT unique,
        password TEXT)
''')
cursor.execute('''
    INSERT INTO users(name,email,password) VALUES(?,?,?)''',
               ('Luke','luke@skywalker.com','iamurfather'))
cursor.execute('''
    INSERT INTO users(name,email,password) VALUES(?,?,?)''',
               ('Darth Vader','darth@vader.com','darkside'))
conn.commit()
# Retrieving some data
user_id=1
# select one user
cursor.execute('''SELECT name,email,password FROM users WHERE id=?''',(user_id,))
# first element of the selected data is returned by fecthone() function
user1=cursor.fetchone()
print('>>>fetch one user:')
print('name of the user #'+str(user_id)+' : '+str(user1[0]))
print('email of the user #'+str(user_id)+' : '+str(user1[1]))
# select all users
cursor.execute('''SELECT name,email,password FROM users''')
allusers=cursor.fetchall()
print('>>>fetch all users:')
for user in allusers:
    print('{0} : {1}, {2}'.format(user[0],user[1],user[2]))
# Deleting or updating some data
new_email='vader@deathstar.com'
userid=2
cursor.execute('''UPDATE users SET email = ? WHERE id = ?''',
               (new_email, userid))
# display users after update
cursor.execute('''SELECT name,email,password FROM users''')
allusers=cursor.fetchall()
print('>>>users after update:')
for user in allusers:
    print('{0} : {1}, {2}'.format(user[0],user[1],user[2]))
del_userid=1
cursor.execute('''DELETE FROM users WHERE id = ?''', (del_userid,))
# display users after delete
cursor.execute('''SELECT name,email,password FROM users''')
allusers=cursor.fetchall()
print('>>>users after delete:')
for user in allusers:
    print('{0} : {1}, {2}'.format(user[0],user[1],user[2]))
conn.commit()
conn.close()