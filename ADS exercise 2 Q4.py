# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 15:44:52 2023

@author: HP
"""
# doing all the imports HERE
import numpy as np
import matplotlib.pyplot as plt

def fsquare(x, l):
    f = nterm(x, l, 1) + nterm(x, l, 3) + nterm(x, l, 5) + nterm(x, l, 7) \
+ nterm(x, l, 9) + nterm(x, l, 11) + nterm(x, l, 13) \
+ nterm(x, l, 15) + nterm(x, l, 17)
    return f

def nterm(x, l, n):
    t = np.sin(2.0*n*np.pi*x / l) / n
    return t

def square(x, l):
# calculate a sine wave
    f = np.sin(x)
# use the sign function (+1 for positive numbers, -1 for negative numbers
# to convert into a square wave
    f = np.sign(f)
    return f

l = 2.0*np.pi # wavelength of the square wave
x = np.linspace(-2.0*np.pi, 2.0*np.pi, 10000)
plt.figure()

# plot square wave and approximation
plt.plot(x, fsquare(x, l), label="Fourier")
plt.plot(x, square(x, l), label="square")

# limits, labels and legend
plt.xlim(-2.0*np.pi, 2.0*np.pi)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.show()
