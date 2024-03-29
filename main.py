import graph
import compute
import numpy as np
import tkinter as tk
from tkinter import ttk
import math 
from tabulate import tabulate
import function

# window = tk.Tk()

# Global to all Graphs
rangeLow = 0
rangeHigh = 20
step = 0.005


sin = 0
amp = 7
damp = 0.8
period = 2 * math.pi
shift = 0
elevation = 0

damp_wave = function.Damp_Wave(sin, amp, damp, period, shift, elevation)

compute_result = compute.compute_wave_damp(damp_wave, rangeLow, rangeHigh, step)

# with open("output.csv", "w") as file:
#     for i in range(len(compute_result[0])):
#         file.write(str(compute_result[0][i]) + "," + str(compute_result[1][i]) + "\n")


# for result in compute_result[1]:
#     print(result) 

wave = function.Wave(0, amp, period, 0, 0)
wave_compute = compute.compute_wave(wave, rangeLow, rangeHigh, step)

expon = function.Exponential(amp, damp, 0)
expon_compute = compute.compute_exponential(expon, rangeLow, rangeHigh, step)

print('\nStats: ')

table = [['Y Max', 'b'], ['Tangent Max', 'd']]
print(tabulate(table, tablefmt="grid"))
# graph.draw([[wave_compute[0], wave_compute[1], 'b-']])
graph.draw([[compute_result[0], compute_result[1], 'r-'], [wave_compute[0], wave_compute[1], 'b-'], [expon_compute[0], expon_compute[1], 'g-']], ['Damponed Wave', 'Cos wave', 'Exponential decay'])

# wave = function.Linear_Bounce(5, 10, 10, 5, 2, 2)

# compute_result_bounce = compute.compute_linear_bounce(wave, rangeLow, rangeHigh, step)

# graph.draw([[compute_result_bounce[0], compute_result_bounce[1], 'r-']], ['Bouncy'])

window.mainloop()