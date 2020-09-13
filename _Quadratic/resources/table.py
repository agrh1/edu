"""
Модуль для создания и конфигурации БД
"""
import sqlite3 

conn = sqlite3.connect('data.db')
cur = conn.cursor()

create_coeffs = 'CREATE TABLE IF NOT EXISTS coeffs (A INT, B INT, C INT)'
cur.execute(create_coeffs)



# НЕОБЯЗАТЕЛЬНОЕ ДЕЙСТВИЕ В КОНТЕКСТЕ SQLITE3
conn.commit()

conn.close()
