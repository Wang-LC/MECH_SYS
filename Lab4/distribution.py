import numpy as np
import matplotlib.pyplot as plt


def randomNumber():
    return sum(np.random.uniform(0, 1, 10))


def distribution():
    sumNumber = []

    for n in range(10000):
        sumNumber.append(randomNumber())

    plt.hist(sumNumber, 50, facecolor='b', edgecolor='k', alpha=0.7)
    plt.xlabel('Sum of random samples')
    plt.ylabel('Times')
    plt.title('Histogram for sum random samples')
    plt.show()


if __name__ == "__main__":
    distribution()