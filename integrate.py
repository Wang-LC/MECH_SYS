import numpy
import random
import matplotlib.pyplot as plt
import math


def func(x):
    return x**2+x+1


def integrate(f, j, k, integral=100):
    a = min()
    delta = numpy.linspace(a, b, integral)
    s = 0
    for x in range(integral-1):
        s += (f(delta[x]) + f(delta[x + 1])) * (delta[x + 1] - delta[x]) / 2
    return s


def integrate_mc(f, a, b, c, d, sample=10000):
    n = 0
    for i in range(sample):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        if abs(y) <= abs(f(x)):
            if 0 <= y <= f(x):
                n += 1
            if 0 >= y >= f(x):
                n -= 1
    area = n / sample * (b - a) * (d - c)
    if c > 0 and d > 0:
        return area + (b-a)*c
    elif c < 0 and d < 0:
        return area + (b-a)*d
    else:
        return area


def error_plot():
    int_error = []
    mc_error = []
    sample_num = []
    for i in range(6):
        rei = abs(integrate(func, 10, 20, int(pow(10, i))) - 2493.333)
        mc = abs(integrate_mc(func, 10, 20, 100, 450, int(pow(10, i)))-2493.333)
        int_error.append(rei)
        mc_error.append(mc)
        sample_num.append(pow(10,i))
    x = [str(i) for i in sample_num]
    plt.plot(x, int_error, '*-', label='Reimann error')
    plt.plot(x, mc_error, 'x-', label='MC error')
    plt.legend()
    plt.xlabel('number of intervals or samples')
    plt.ylabel('Absolute Error')
    plt.title('ERROR')
    plt.show()


def approximate_pi(n):
    return 4*integrate_mc(lambda x: math.sqrt(1-x**2), 0, 1, 0, 1, n)


if __name__ == "__main__":
    error_plot()


