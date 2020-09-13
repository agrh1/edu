"""поиск количества корней квадратного уравнения по заданным коэффициентам."""
class QuadraticFunc:
    """descr_eq"""
    def __init__(self, a_coeff, b_coeff, c_coeff):
        """method"""
        self.__a = a_coeff
        self.__b = b_coeff
        self.__c = c_coeff

    def solve(self) -> int:
        """method"""
        if self.__a == 0:
            return self.__linear()
        return self.__quadratic()

    def __linear(self) -> int:
        """method"""
        if self.__b == 0:
            return 0
        return 1

    def __quadratic(self) -> int:
        """method"""
        descr_eq = self.__b ** 2 - 4 * self.__a * self.__c
        if descr_eq > 0:
            return 2
        if descr_eq == 0:
            return 1
        return 0

if __name__ == "__main__":
    pass
