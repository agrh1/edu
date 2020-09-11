"""docstring"""
from flask import Flask
from flask_restful import Api
from resources.res import GrabQ, SolveQ
app = Flask(__name__) # Общая конфигурация приложения Flask
api = Api(app) # Подключение функционала RESTful API

# Добавим ресурс в api
api.add_resource(GrabQ, "/grab")
api.add_resource(SolveQ, "/solve")

if __name__ == "__main__":
    app.run(port=8080, debug=True)
