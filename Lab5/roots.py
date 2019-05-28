import math
from complex import Complex


def roots(a, b, c):
    n = b ** 2 - 4 * a * c
    if n > 0:
        return (-b + math.sqrt(n)) / (2 * a), (-b - math.sqrt(n)) / (2 * a)
    elif n == 0:
        return -b / (2 * a)
    else:
        real = -b/(2*a)
        imag = math.sqrt(-n) / (2 * a)
        return Complex(real, imag), Complex(real, -imag)


if __name__ == "__main__":
    print(roots(1, 1, 1))
