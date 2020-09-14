# import sqlite3
from db import db
# Модель пользователя
class UserModel:
    #Внушний атрибут класса , указывающий на имя таблицы
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # Вводим новое поле
    username = db.Column(db.String(50))
    password =  db.Column(db.String(50))
    def __init__(self, _id, username, password):
        self.id = _id 
        self.username = username
        self.password = password
    def insert(self):
        db.session.add(self)
        db.session.commit()
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()
        # insert_query = "INSERT INTO {} VALUES(NULL, ? ,?)".format(self.__tablename__) 
        # cur.execute(insert_query, (self.username, self.password))
        # conn.commit()
        # conn.close()
    @classmethod
    def search_username(cls, username):
        return cls.query.filter_by(username=username).first()
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()
        # select_query = "SELECT * FROM {} WHERE username=?".format(cls.__tablename__)
        # sql_row = cur.execute(select_query, (username, )).fetchone() # (1, "Bob", "asp[daspd")
        # if sql_row:
        #     user = cls(sql_row[0], sql_row[1], sql_row[2])
        # else:
        #     user = None 
        # conn.close()
        return user
    @classmethod
    def search_id(cls, _id) :
        return cls.query.filter_by(id=_id).first()
        # conn = sqlite3.connect('data.db')
        # cur = conn.cursor()
        # select_query = "SELECT * FROM {} WHERE id=?".format(cls.__tablename__)
        # sql_row = cur.execute(select_query, (_id, )).fetchone() # [(1, "Bob", "asp[daspd")]
        # if sql_row:
        #     user = cls(sql_row[0], sql_row[1], sql_row[2])
        # else:
        #     user = None 
        # conn.close()
        return user

