#!/usr/bin/python3

import os
import re
import numpy as np
import sys


class Simulator:
    def __init__(self, instance):
        self.ins = instance

    def evaluate(self, path) :
        with open('waypoints', 'w') as f :
            for i in path :
                f.write(str(i).replace('(', '').replace(')', '').replace(',', '') + '\n')

        cmd = 'simulator waypoints %s' % (str(self.ins))
        p = os.popen(cmd)
        data = p.readlines()[1]
        return float(re.findall(r'\d+\.?\d*', data)[0])


def find_better(ins, calls):
    simulate = Simulator(ins)
    cost = []
    x = np.random.uniform(-10, 10, calls)
    y = np.random.uniform(-10, 10, calls)
    for i in range(calls):
            path = [(-10, -10), (x[i], y[i]), (10, 10)]
            cost.append(simulate.evaluate(path))
    n = cost.index(min(cost))
    x_better = x[n]
    y_better = y[n]

    with open('better_waypoints', 'w') as f:
        f.write('-10 -10\n%s %s\n10 10' % (x_better, y_better))


if __name__ == '__main__' :
    # w = [(-10, -10), (-10, 2), (10, 10)]
    # s = Simulator(10)
    # print(s.evaluate(w))
    find_better(sys.argv[1], 60)
