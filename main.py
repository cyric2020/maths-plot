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
rangeHigh = 10
step = 0.001


sin = 0
amp = 1
damp = 0.8
period = 2 * math.pi
shift = 0
elevation = 0

damp_wave = function.Damp_Wave(sin, amp, damp, period, shift, elevation)

compute_result = compute.compute_wave_damp(damp_wave, rangeLow, rangeHigh, step)

wave = function.Wave(0, 1, period, 0, 0)
wave_compute = compute.compute_wave(wave, rangeLow, rangeHigh, step)

print('\nStats: ')

table = [['Y Max', 'b'], ['Tangent Max', 'd']]
print(tabulate(table, tablefmt="grid"))

graph.draw([[compute_result[0], compute_result[1],'r-'], [wave_compute[0], wave_compute[1], 'b-']])

# window.mainloop()