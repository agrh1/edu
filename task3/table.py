import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)'
cur.execute(create_table)

create_table = 'CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY KEY, mark TEXT, max_speed INTEGER, distance INTEGER, handler TEXT, stock TEXT)'
cur.execute(create_table)


# добавляем пользователя
# insert_query = 'INSERT INTO users VALUES(?,?,?)' 
# user = [1, 'Alex', 'qwerty']

# cur.execute(insert_query, (user[0],user[1], user[2]))
conn.commit()
conn.close()


