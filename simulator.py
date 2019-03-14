#!/usr/bin/python3

import os
import re
import numpy as np
import scipy.optimize as opt
import sys


class Simulator :
    def __init__(self, instance) :
        self.ins = instance

    def evaluate(self, path) :
        with open('waypoints', 'w') as f :
            for i in path :
                f.write(str(i).replace('(', '').replace(')', '').replace(',', '') + '\n')

        cmd = 'simulator waypoints %s' % (str(self.ins))
        p = os.popen(cmd)
        data = p.readlines()[1]
        return float(re.findall(r'\d+\.?\d*', data)[0])


def find_better(ins) :
    simulate = Simulator(ins)
    n = 150.0
    for i in np.linspace(0, 20, 21):
        for j in np.linspace(0, 20, 21):
            path = [(-10, -10), (-10 + i, -10 + j), (10, 10)]
            if simulate.evaluate(path) < float(n):
                n = simulate.evaluate(path)
                x_better = -10 + i
                y_better = -10 + j
    # x = [-10, 10]
    # y = [-10, 10]
    # x_better = opt.fminbound(lambda x1 : func(x1, -1), -10, 10)
    # y_better = opt.fminbound(lambda y1 : func(x_better, y1), -10, 10)

    with open('better_waypoints', 'w') as f :
        f.write('-10 -10\n%s %s\n10 10' % (x_better, y_better))
    # print(simulate.evaluate([(-10, -10), (x_better, y_better), (10, 10)]))


# def func(x_value, y_value):
#     simulate = Simulator(10)
#     # for i in range(len(x_value)):
#     #     for j in range(len(y_value)):
#     w = [(-10, -10), (x_value, y_value), (10, 10)]
#     return float(simulate.evaluate(w))


if __name__ == '__main__' :
    # w = [(-10, -10), (-10, 2), (10, 10)]
    # s = Simulator(10)
    # print(s.evaluate(w))
    find_better(10)
