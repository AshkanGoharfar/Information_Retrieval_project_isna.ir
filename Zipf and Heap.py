from Create_inverted_index import *
import numpy as np
import matplotlib.pyplot as plt
import math

inverted_index = extract_inverted_index()


freq = []

for item in inverted_index:
    freq.append(inverted_index[item]['freq'])


def heaps_law():
    x = []
    y = []
    token = 0
    for i in range(1, len(freq)):
        x.append(math.log10(i))
        token += freq[i - 1]
        y.append(math.log10(token))

    area = np.pi * 3
    # Plot
    plt.scatter(x, y, s=area, alpha=0.5)

    plt.title('Comaparison dataset columns')
    plt.xlabel('vocab size')
    plt.ylabel('number of tokens')

    plt.plot()
    plt.show()


def zipf_law():
    x = []
    y = []
    token = 0
    for i in range(len(freq)):
        x.append(math.log10(freq[i]))
        y.append(math.log10(freq[0] / freq[i]))
    area = np.pi * 3

    # Plot
    plt.scatter(x, y, s=area, alpha=0.5)

    plt.title('Comaparison dataset columns')
    plt.xlabel('log 10 rank')
    plt.ylabel('log 10 cfi')

    plt.plot()
    plt.show()


zipf_law()

heaps_law()
