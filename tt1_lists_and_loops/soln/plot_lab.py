import math
import pylab as plt
import numpy as np

def sinc(x):
    if x != 0:
        return math.sin(x) / x;
    else:
        return 1;

def plot_sinc():
    # Compute the X's
    X = []
    for x in range(-10, 10, 1):
        X.append(x)

    # Compute the Y's
    Y = []
    for x in X:
        Y.append(sinc(x))

    plt.plot(X, Y)
    plt.show()


def plot_sinc_revised(incr):
    # Compute the X's and the Y's
    X = []
    Y = []
    for x in np.arange(-10, 10, incr):
        X.append(x)
        Y.append(sinc(x))

    plt.plot(X, Y)
    plt.show()

