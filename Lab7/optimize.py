import numpy as np
import random
import scipy.optimize as opt
import matplotlib.pyplot as plt


def optimize_step(f, bounds, n):
    try:
        f(1)
    except TypeError:
        raise TypeError('Please enter a defined function')

    try:
        a = min(bounds[0], bounds[1])
        b = max(bounds[0], bounds[1])
    except TypeError:
        raise TypeError('please enter a tuple')

    # set right max and min
    x_value = np.linspace(a, b, n)
    y_array = []
    # set x y array
    for i in x_value:
        y_array.append(f(i))

    index = y_array.index(max(y_array))
    return x_value[index]


def optimize_random(f, bounds, n):
    try:
        f(1)
    except TypeError:
        raise TypeError('Please enter a defined function')

    try:
        a = min(bounds[0], bounds[1])
        b = max(bounds[0], bounds[1])
    except TypeError:
        raise TypeError('please enter a tuple')

    x_value = []
    for n in range(n):
        x_value.append(random.uniform(a, b))
    # get random x array
    y_array = []
    for i in x_value:
        y_array.append(f(i))

    index = y_array.index(max(y_array))
    return x_value[index]


def plot_performance():
    x = np.linspace(10, 1000, 20)
    step_error = []
    random_error = []
    for i in x:
        step_error.append(abs(optimize_step(func, (0, 5), int(i)) - 1))
        random_error.append(abs(optimize_random(func, (0, 5), int(i)) - 1))

    f_error = opt.fmin(neg_func, 0, full_output=True, disp=False)[0]-1
    # get fmin error
    f_eva = opt.fmin(neg_func, 0, full_output=True, disp=False)[3]
    # get fmin evaluation
    plt.plot(x, step_error, '*-', label='optimize_step')
    plt.plot(x, random_error, 'x-', label='optimize_random')
    plt.plot(f_eva, f_error, 'o', label='fmin')
    plt.legend()
    plt.xlabel('the number of function evaluations(steps)')
    plt.ylabel('Absolute Error')
    plt.title('The performance of the three approaches as a function')
    plt.show()


def func(x):
    return -(x-1)**2 + 5


def neg_func(x):
    return (x-1)**2 - 5


def optimize_md(f, bounds):
    n = 1000  # num of steps
    m = len(bounds)
    point = []
    for i in range(m):  # use the first value as initial value for each
        point.append(bounds[i][0])

    for i in range(m):  # find the x value(iterable) for each
        y_value = []
        x_point = []
        for j in range(n):
            x_point.append(point[i])
            try:
                y_value.append(f(*point))
            except TypeError:
                raise TypeError('Please enter a defined function with same number of tuple')

            point[i] += (bounds[i][1] - bounds[i][0])/n
        point[i] = x_point[y_value.index(max(y_value))]
        # set the x value as the value of the largest one
    return tuple(point)


def f1(a, b, c, d):
    return -(a-1)**2 + 5*b - c**2 + 4*d


def f2(a, b, c, d, e):
    return (a-2)**2 - (b - 1) ** 2 + 5 * c - d ** 2 + 4 * e


if __name__ == '__main__':
    plot_performance()
    print(optimize_md(func, [(0, 5)]))
    print(optimize_md(f1, [(-1, 1), (-2, 2), (2, 4), (0, 2)]))
    print(optimize_md(f2, [(10, 12), (-1, 1), (-2, 2), (2, 4), (0, 2)]))

