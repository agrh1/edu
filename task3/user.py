"""модуль пользователя. Модель и Ресурс"""
import sqlite3
from flask_restful import Resource, reqparse

class User:
    """описание класса User (модель пользователя)"""
    __tablename__ = "users"
    def __init__(self, _id, username, password):
        """конструктор класса"""
        self.id = _id
        self.username = username
        self.password = password
    @classmethod
    def search_username(cls, username):
        """поиск пользователя в БД по имени"""
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        select_query = "SELECT * FROM {} WHERE username=?".format(cls.__tablename__)
        sql_row = cur.execute(select_query, (username, )).fetchone()
        if sql_row:
            user = cls(sql_row[0], sql_row[1], sql_row[2])
        else:
            user = None
        conn.close()
        return user
    @classmethod
    def search_id(cls, _id):
        """поиск пользователя в БД по id"""
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        select_query = "SELECT * FROM {} WHERE id=?".format(cls.__tablename__)
        sql_row = cur.execute(select_query, (_id,)).fetchone()
        if sql_row:
            user = cls(sql_row[0], sql_row[1], sql_row[2])
        else:
            user = None
        conn.close()
        return user

class UserResource(Resource):
    """описание класса User (ресурс пользователя)"""
    __tablename__ = "users"
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help='Username field required')
    parser.add_argument("password", type=str, required=True, help='Password field required')
    def post(self):
        """добавить пользователя в БД"""
        request_body = UserResource.parser.parse_args()
        if User.search_username(request_body['username']):
            return {"Error" : "User already exists"}, 400
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        insert_query = "INSERT INTO {} VALUES(NULL,?,?)".format(self.__tablename__)
        cur.execute(insert_query, (request_body['username'], request_body['password']))
        conn.commit()
        return {"Message" : "User created. Try to auth"}, 201
