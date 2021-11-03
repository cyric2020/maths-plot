import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def draw(comb):
    fig, ax = plt.subplots()
    for graph in comb:
        lns1 = plt.plot(graph[0], graph[1], graph[2], linewidth=1)
        plt.ylabel('y')
        plt.xlabel('x')

        ax.set_axisbelow(True)

        ax.grid()
        ax.minorticks_on()

        ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
        ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
        plt.draw()
    plt.show()