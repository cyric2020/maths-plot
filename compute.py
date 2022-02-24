import numpy as np
import math
import function

def computeFunc(func, rangel, rangeh, step=1):
    x = np.array([])
    y = np.array([])
    i = rangel
    while i < rangeh:
        x = np.append(x, i)
        y = np.append(y, np.sin(i))
        i += step
    return [x, y]

def compute_wave_damp(wave, rangeL=0, rangeH=10, step=1):
    A, b, c, d, f, sin = wave.A, wave.b, wave.c, wave.d, wave.f, wave.sin
    x = np.array([])
    y = np.array([])
    i = rangeL
    while i < rangeH:
        print('Calculating graph ' + str(round((i - rangeL) * 100 / (rangeH - rangeL), 2)) + '%', end="\r", flush=True)
        x = np.append(x, i)
        if sin : y = np.append(y, A*np.exp(-b*i)*np.sin(c*i+d)+f)
        if not sin : y = np.append(y, A*np.exp(-b*i)*np.cos(c*i+d)+f)
        i += step
    print('')
    return [x, y]

def compute_wave(wave, rangeL=0, rangeH=10, step=1):
    A, b, c, d, sin = wave.A, wave.b, wave.c, wave.d, wave.sin
    x = np.array([])
    y = np.array([])
    i = rangeL
    while i < rangeH:
        print('Calculating graph ' + str(round((i - rangeL) * 100 / (rangeH - rangeL), 2)) + '%', end="\r", flush=True)
        x = np.append(x, i)
        if sin : y = np.append(y, A*np.sin(b*i+c)+d)
        if not sin : y = np.append(y, A*np.cos(b*i+c)+d)
        i += step
    print('')
    return [x, y]

def compute_exponential(wave, rangeL=0, rangeH=10, step=1):
    A, b, c = wave.A, wave.b, wave.c
    x = np.array([])
    y = np.array([])
    i = rangeL
    while i < rangeH:
        print('Calculating graph ' + str(round((i - rangeL) * 100 / (rangeH - rangeL), 2)) + '%', end="\r", flush=True)
        x = np.append(x, i)
        y = np.append(y, A*np.exp(-b*i)+c)
        i += step
    print('')
    return [x, y]

def compute_linear_bounce(wave, rangeL=0, rangeH=0, step=1):
    BugA_X, BugA_Y, BugB_X, BugB_Y, n, m = wave.BugA_X, wave.BugA_Y, wave.BugB_X, wave.BugB_Y, wave.n, wave.m
    x = np.array([])
    y = np.array([])
    i = rangeL
    while i < rangeH:
        print('Calculating graph ' + str(round((i - rangeL) * 100 / (rangeH - rangeL), 2)) + '%', end="\r", flush=True)
        x = np.append(x, i)

        bugAX = BugA_X+i*i
        bugBX = BugB_X+i*i

        y = np.append(y, math.sqrt(bugAX*bugAX+bugBX*bugBX))
        i += step
    print('')
    return [x, y]