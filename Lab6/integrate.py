import numpy
import random
import matplotlib.pyplot as plt
import math


def func(x):
    return x**2-3


def integrate(f, j, k, integral=100):  # Q1
    try:
        f(1)
    except TypeError:
        raise TypeError('enter a def function')
    try:
        a = min([float(j), float(k)])
        b = max([float(j), float(k)])
    except TypeError:
        raise TypeError('please enter number')

    delta = numpy.linspace(a, b, integral)
    s = 0
    for x in range(integral-1):
        s += (f(delta[x]) + f(delta[x + 1])) * (delta[x + 1] - delta[x]) / 2
    return s


def integrate_mc(f, a, b, T, sample=100000):  # Q2
    try:
        f(1)
    except TypeError:
        raise TypeError('enter a def function')
    try:
        a = float(a)
        b = float(b)
    except TypeError:
        raise TypeError('please enter number')
    try:
        c = min([T[0], T[1]])
        d = max([T[0], T[1]])
    except TypeError:
        raise TypeError('please enter a tuple')
    count = 0
    for i in range(sample):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        if abs(y) <= abs(f(x)):
            if 0 <= y <= f(x):
                count += 1
            if 0 >= y >= f(x):
                count -= 1
    area = count / sample * (b - a) * (d - c)
    if c > 0 and d > 0:
        return area + (b-a)*c
    elif c < 0 and d < 0:
        return area + (b-a)*d
    else:
        return area


def error_plot():  # Q3 plot the graph
    int_error = []
    mc_error = []
    sample_num = []
    for i in numpy.linspace(10, 100000, 30):
        rei = abs(integrate(func, 10, 20, int(i)) - 2493.333)
        mc = abs(integrate_mc(func, 10, 20, (0, 450), int(i))-2493.333)
        int_error.append(rei)
        mc_error.append(mc)
        sample_num.append(int(i))
    plt.plot(sample_num, int_error, '*-', label='Reimann error')
    plt.plot(sample_num, mc_error, 'x-', label='MC error')
    plt.legend()
    plt.xlabel('number of intervals or samples')
    plt.ylabel('Absolute Error')
    plt.title(' the convergence behavior of the two functions \n (MC function has some noise even with large samples)')
    plt.show()


def approximate_pi(n):  # Q4
    return 4*integrate_mc(lambda x: math.sqrt(1-x**2), 0, 1, (0, 1), n)


if __name__ == "__main__":
    print(integrate(func, -3, 3, 1000))
    print(integrate_mc(func, -3, 3, (-3, 6), 100000))
    print(approximate_pi(100))

