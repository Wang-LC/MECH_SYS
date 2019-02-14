import cmath
from complex import Complex


def roots(a, b, c):
    x = (-b + cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    y = (-b - cmath.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    # if x == y:
    #     return Complex(x.real, x.imag), None
    # else:
    #     return Complex(x.real, x.imag), Complex(y.real, y.imag)
    return x, y


if __name__ == "__main__":
    #x, y = roots(1, 2, 3)
    print(roots(1, 1, 1))
