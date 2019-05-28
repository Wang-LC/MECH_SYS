
class Complex:
    # Q1
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    # Q2
    def __repr__(self):
        return '({0} {1} {2}i)'.format(self.re, '-' if self.im < 0 else '+', abs(self.im))

    def __str__(self):
        return self.__repr__()

    # Q4 addition
    def __add__(self, other):
        try:
            d = Complex(self.re + other.re, self.im + other.im)
        except:
            return self + Complex(other)
        return d

    def __radd__(self, other):
        return self + other

    # Q4 subtraction
    def __sub__(self, other):
        d = Complex()
        try:
            d.re = self.re - other.re
            d.im = self.im - other.im
        except:
            return self - Complex(other)
        return d

    def __rsub__(self, other):
        return -self + other

    # Q5 multiplication
    def __mul__(self, other):
        d = Complex()
        try:
            d.re = (self.re * other.re) - (self.im * other.im)
            d.im = (self.im * other.re) + (self.re * other.im)
        except:
            return self * Complex(other)
        return d

    def __rmul__(self, other):
        return self * other

    # Q5 division
    def __truediv__(self, other):
        d = Complex()
        try:
            n = other.re**2 + other.im**2
            d.re = ((self.re * other.re)+(self.im * other.im))/n
            d.im = ((self.im * other.re)-(self.re * other.im))/n
        except:
            return self / Complex(other)
        return d

    def __rtruediv__(self, other):
        return self / other

    # Q6 negation
    def __neg__(self):
        return Complex(re=-self.re, im=-self.im)

    # Q6 conjugate
    def __invert__(self):
        return Complex(re=self.re, im=-self.im)


if __name__ == "__main__":
    a = Complex(1, 1)
    b = Complex(1, 1)
    print(a*b)
    print(a/b)
    print(a+1)
    print(~a)
    print(-a)
    print(complex(1, 2) / complex(3, 4))
    print(Complex(1, 2)/Complex(3, 4))
