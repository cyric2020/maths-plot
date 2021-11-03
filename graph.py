import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def draw(comb, names):
    sns.set_theme(style="darkgrid")
    for graph in comb:
        x = graph[0]
        y = graph[1]
        plt.plot(x, y)
        plt.legend(names, ncol=2, loc='upper left')
        plt.draw()
    plt.show()

# def draw(comb):
#     fig, ax = plt.subplots()
#     for graph in comb:
#         x = graph[0]
#         y = graph[1]
#         color = graph[2]
#         # use seaborn to plot the graph with the color
#         sns.lineplot(x=x, y=y, ax=ax)
#     #     lns1 = plt.plot(x, y, color, linewidth=1)
#     #     plt.ylabel('y')
#     #     plt.xlabel('x')

#     #     ax.set_axisbelow(True)

#     #     ax.grid()
#     #     ax.minorticks_on()

#     #     ax.grid(which='major', linestyle='-', linewidth='0.5', color='red')
#     #     ax.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
#     #     plt.draw()
#     # plt.show()