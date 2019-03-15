#!/usr/bin/python3

from simulator import Simulator
import math
import numpy as np
import sys


def main(ins, calls):
    r = int(math.sqrt(calls))
    simulate = Simulator(ins)
    cost = []
    x = []
    y = []
    for i in np.linspace(-10, 10, r):
        for j in np.linspace(-10, 10, r):
            path = [(-10, -10), (i, j), (10, 10)]
            cost.append(simulate.evaluate(path))
            x.append(i)
            y.append(j)
    n = cost.index(min(cost))
    x_better = x[n]
    y_better = y[n]

    with open('best_waypoints', 'w') as f :
        f.write('-10 -10\n%s %s\n10 10' % (x_better, y_better))


if __name__ == '__main__' :
    main(sys.argv[1], int(sys.argv[2]))