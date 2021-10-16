import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def draw(comb):
    for graph in comb:
        lns1 = plt.plot(graph[0], graph[1], graph[2], linewidth=1)
        plt.ylabel('y')
        plt.xlabel('x')

        plt.draw()
    plt.show()