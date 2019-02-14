from math import pow
import numpy as np
import time
import matplotlib.pyplot as plt


def sortPlot():
    lenList = []
    timeList = []
    sumList = []

    for i in range(6):
        randomList = np.random.uniform(0, 10**7, int(pow(10, i)))
        t0 = time.time()
        sorted(randomList)
        t1 = time.time()
        sum(randomList)
        t2 = time.time()
        sortTime = t1 - t0
        sumTime = t2 - t1
        lenList.append(len(randomList))
        timeList.append(sortTime)
        sumList.append(sumTime)

    x = [str(i) for i in lenList]
    plt.plot(x, timeList, label='sort')
    plt.plot(x, sumList, label='sum')
    plt.legend()
    plt.xlabel('Length of sample')
    plt.ylabel('Time')
    plt.title('Time difference between sum and sort')
    plt.show()


if __name__ == "__main__":
    sortPlot()