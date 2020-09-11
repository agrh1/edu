"""ресурсы принятия запросов"""
import sqlite3
from flask_restful import Resource, reqparse
from models.equation import QuadraticFunc

class GrabQ(Resource):
    """
    Ресурс GrabQ /grab/<list:coeffs>
    принимает аргументы A, B, C
    """
    __tablename__ = 'coeffs'
    parser = reqparse.RequestParser()
    parser.add_argument('A', type=int, required=True, help="A coeff required")
    parser.add_argument('B', type=int, required=True, help="B coeff required")
    parser.add_argument('C', type=int, required=True, help="C coeff required")

    def post(self):
        """method desc"""
        request_body = GrabQ.parser.parse_args()
        coeffs = {'A' : request_body['A'], 'B' : request_body['B'], 'C' : request_body['C'],}
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        delete_query = "DELETE FROM {}".format(self.__tablename__)
        cur.execute(delete_query, ())
        insert_query = "INSERT INTO {} VALUES(?, ?, ?)".format(self.__tablename__)
        cur.execute(insert_query, (coeffs['A'], coeffs['B'], coeffs['C'],))
        conn.commit()
        conn.close()
        return {}, 201

class SolveQ(Resource):
    """
    Ресурс Solve /solve
    решает квадратное уравнение по аргументам из словаря coeffs
    """
    __tablename__ = 'coeffs'
    def get(cls):
        """method desc"""
        conn = sqlite3.connect('data.db')
        cur = conn.cursor()
        select_query = 'SELECT * FROM {}'.format(cls.__tablename__)
        row = cur.execute(select_query, ).fetchone()
        conn.close()
        eq_func = QuadraticFunc(int(row[0]), int(row[1]), int(row[2]))
        res = eq_func.solve()
        return {
            "A" : int(row[0]),
            "B" : int(row[1]),
            "C" : int(row[2]),
            "Nroots": res,
            }, 200

if __name__ == "__main__":
    pass
