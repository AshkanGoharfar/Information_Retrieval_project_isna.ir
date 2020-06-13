from Create_inverted_index import *
import numpy as np
import matplotlib.pyplot as plt
import math

inverted_index = extract_inverted_index()


freq = []

for item in inverted_index:
    freq.append(inverted_index[item]['freq'])


def Heaps_law(k):
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


# def Zipf_law():
    # x = []
    # y = []
    # token = 0
    # for i in range(len(freq)):
    #     x.append(math.log10())


Heaps_law(40)
