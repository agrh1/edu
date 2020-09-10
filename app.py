from flask import Flask , request,jsonify
from flask_restful import Resource, Api , reqparse
from Equation import QuadraticFunc
# Общая конфигурация приложения Flask
app = Flask(__name__)
# Подключение функционала RESTful API
api = Api(app)



# Локальная БД
coeffs = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
    }

# Ресурс Grab /grab/<list:coeffs>
class GrabQ(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('A', type=int, required=True, help="A coeff required")
    parser.add_argument('B', type=int, required=True, help="B coeff required")
    parser.add_argument('C', type=int, required=True, help="C coeff required")
        
    def post(self):
        req_body = GrabQ.parser.parse_args()
        global coeffs
        coeffs = dict(req_body)
        return {}, 201

# Ресурс Solve /solve
class SolveQ(Resource):
    # теперь не нужно использовать @app.route(......)
    # нужно лишь определять методы с названиями HTTP запросов
    # важная вещь - имя метода С МАЛЕНЬКОЙ БУКВЫ
    def get(self):
        # jsonify() больше не нужен, он применяется автоматически flask_restful
        eq = QuadraticFunc(int(coeffs["A"]), int(coeffs["B"]), int(coeffs["C"]))
        res = eq.solve()
        
        return {
            "A" : coeffs["A"],
            "B" : coeffs["B"],
            "C" : coeffs["C"],
            "Nroots": res,
        },200
 
# Добавим ресурс в api
api.add_resource(GrabQ, "/grab")
api.add_resource(SolveQ, "/solve")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
