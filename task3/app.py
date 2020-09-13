"""склад с авто, работа с авто"""
import sqlite3
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from auth_conf import authenticate, identity
from user import UserResource

app = Flask(__name__)
app.secret_key = "AppSecretKey"
jwt = JWT(app, authentication_handler=authenticate, identity_handler=identity)
api = Api(app)
# РЕСУРСЫ
# /register
    # POST
        # {"Message" : "User created. Try to auth"}, 201
        # {"Error" : "User already exists"}, 400
            # {
            #  "username" : "Some user",
            #  "password" : "Some password"
            # }
# /stock  + JWT
    # GET /stock
        # stock, 200
        # {"Error" : "No one autos found in DataBase"}, 400
# /auto/<string:mark>  + JWT
    # GET /auto/<string:mark>
        # info, 200
        # {"Error" : "Auto with that mark not found"}, 404
    # POST /auto/<string:mark>
        # {"Message" : "Auto created"}, 201
        # {"Error" : "Auto with that mark exists"}, 400
            # {
            #  "max_speed" : 280,
            #  "distance" : 400,
            #  "handler" : "Auto Motors",
            #  "stock" : "Germany"
            # }
    # PUT /auto/<string:mark>
        # {"Message" : "Auto updated"}, 202
        # {"Error" : "Auto with that mark not found"}, 404
    # DELETE /auto/<string:mark>
        # {"Message" : "Auto deleted"}, 202
        # {"Error" : "Auto with that mark not found"}, 404
# POST /auth - возвращает JWT
# users=[
#     {
#         "username" : "user",
#         "password" : "qwerty"
#     }
# ]
# stock_info=[
#     {
#         "mark" : "bmw",
#         "desc" : {
#              "max_speed" : 280,
#              "distance" : 400,
#              "handler" : "Auto Motors",
#              "stock" : "Germany"
#             }
#     }
# ]
class Stock(Resource):
    """class Склад, хранит автомобили"""
    __tablename__ = 'stock'
    @jwt_required()
    def get(self):
        """выдать состояние склада"""
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        select_query = "SELECT * FROM {} ".format(self.__tablename__)
        stock_info = cur.execute(select_query).fetchall()
        conn.commit()
        if stock_info:
            return {"stock_info" : stock_info}, 200
        return {"Error" : "No one autos found in DataBase"}, 400

class Auto(Resource):
    """Ресурс Авто. поиск, обновление, добавление и удаление из БД"""
    parser = reqparse.RequestParser()
    __tablename__ = 'stock'

    @classmethod
    def search_car(cls, mark):
        '''поиск авто по марке'''
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        select_query = "SELECT * FROM {} WHERE mark=?".format(cls.__tablename__)
        car = cur.execute(select_query, (mark, )).fetchall()
        conn.commit()
        if car:
            return car
        return False

    @jwt_required()
    def get(self, mark):
        """выдать авто по марке"""
        if Auto.search_car(mark):
            return Auto.search_car(mark), 200
        return {"Error" : "Auto with that mark not found"}, 404

    @jwt_required()
    def post(self, mark):
        """внести данные по марке в БД"""
        if Auto.search_car(mark):
            return {"Error" : "Auto with that mark exists"}, 400
        req_body = request.get_json()
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        insert_query = "INSERT INTO {} VALUES(NULL,?,?,?,?,?)".format(self.__tablename__)
        (cur.execute(insert_query, (mark, req_body["max_speed"],
                                    req_body["distance"], req_body["handler"],
                                    req_body["stock"])))
        conn.commit()
        return {"Message" : "Auto created"}, 201

    @jwt_required()
    def put(self, mark):
        """обновить инфо об авто по марке"""
        if Auto.search_car(mark):
            req_body = request.get_json()
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()
            update_query = "UPDATE {} SET max_speed=?, distance=?, handler=?, stock=? WHERE mark=?".format(self.__tablename__)
            (cur.execute(update_query, (req_body["max_speed"],
                                        req_body["distance"], req_body["handler"],
                                        req_body["stock"], mark)))
            conn.commit()
            return {"Message" : "Auto updated"}, 202
        return {"Error" : "Auto with that mark not found"}, 404

    @jwt_required()
    def delete(self, mark):
        """удалить авто по марке"""
        if Auto.search_car(mark):
            conn = sqlite3.connect('data.db')
            cur = conn.cursor()
            delete_query = "DELETE FROM {} WHERE mark=?".format(self.__tablename__)
            cur.execute(delete_query, (mark, ))
            conn.commit()
            return {"Message" : "Auto deleted"}, 202
        return {"Error" : "Auto with that mark not found"}, 404

api.add_resource(UserResource, "/register")
api.add_resource(Stock, "/stock")
api.add_resource(Auto, "/auto/<string:mark>")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
