from flask import Flask , request,jsonify
from flask_restful import Resource, Api , reqparse
from models.equation import QuadraticFunc
from resources.res import GrabQ, SolveQ
import resources.table
app = Flask(__name__) # Общая конфигурация приложения Flask
api = Api(app) # Подключение функционала RESTful API

# Локальная БД
coeffs = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
    }

# Добавим ресурс в api
api.add_resource(GrabQ, "/grab")
api.add_resource(SolveQ, "/solve")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
