import matplotlib.pyplot as plt
import numpy as np
import math


def sinWave():
    x = np.linspace(0, 4 * math.pi, 1000)
    plt.plot(x, np.sin(x), 'r--')
    plt.axis([0, 4*math.pi, -1, 1])
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Sin Wave')
    plt.show()


if __name__ == "__main__":
    sinWave()