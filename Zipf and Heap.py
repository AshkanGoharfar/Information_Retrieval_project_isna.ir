from Create_inverted_index import *
import numpy as np
import matplotlib.pyplot as plt
import math

inverted_index = extract_inverted_index()


def Heaps_low(k):
    # # vocabulary size
    # m = len(extract_inverted_index())
    #
    # # number of tokens
    # t = len(contents)
    #
    # # static coefficient
    # b = 0.5
    #
    # x = math.log10(t)
    # y = math.log10(m)
    # area = np.pi * 3
    #
    # # Plot
    # plt.scatter(x, y, s=area, alpha=0.5)
    #
    # plt.title('Comaparison dataset columns')
    # plt.xlabel('vocab size')
    # plt.ylabel('number of tokens')
    #
    # plt.plot()
    # plt.show()

    i = 0
    words = set()
    for word in inverted_index:
        words.add(word)
        i += 1
        print(i, len(words))


Heaps_low(40)