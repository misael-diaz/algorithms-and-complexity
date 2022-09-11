#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Algorithms and Complexity                                 February 23, 2022
IST 4310
Prof. M Diaz-Maldonado

Synopsis:
Shows matplotlib's pyplot can be used for plotting the (x, y) coordinates.

Copyright (c) 2022 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

References:
[0] JJ McConnell, Analysis of Algorithms, 2nd edition, 2007
[1] R Johansson, Numerical Python: Scientific Computing and Data
    Science Applications with NumPy, SciPy, and Matplotlib, 2nd edition
"""

from numpy import array
from matplotlib import pyplot as plt

# defines the particle positions as a list of (x, y) coordinates
P = [
    (2,  7), ( 4, 13), ( 5, 7), (10,  5), (13,  9), (15, 5),
    (17, 7), (19, 10), (22, 7), (25, 10), (29, 14), (30, 2)
]


""" plots the coordinates for visualization """

# closes all figures and enables interactive plotting
plt.close('all')
plt.ion()
# creates a figure and a set of axes
fig, ax = plt.subplots()
# creates a numpy array from the list and unpacks into `x' and `y' vectors
x, y = array(P).T
# plots the coordinates as symbols (no lines connecting them)
ax.plot(x, y, marker='*', markersize=12, color='black', linestyle='')
# sets the axes labels
ax.set_xlabel('x')
ax.set_ylabel('y')
