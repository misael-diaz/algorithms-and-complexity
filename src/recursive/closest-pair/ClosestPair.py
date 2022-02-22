#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Algorithms and Complexity                                 February 20, 2022
IST 3498
Prof. M Diaz-Maldonado

Synopsis:
Divide and Conquer Algorithms. Closest Pair Problem. Partitions the
particles into quadrants and plots their coordinates in a 2D plot.


Copyright (c) 2022 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] JJ McConnell, Analysis of Algorithms, 2nd edition, 2007.
"""


# imports the ceiling function
from math import ceil
# imports Numerical Python (numpy) to use arrays
import numpy as np
# imports Python's Matplotlib library for visualization
import matplotlib as mpl
# imports pyplot for plotting on the same figure
from matplotlib import pyplot as plt


# defines the particle positions as a list of (x, y) coordinates
Ps = [
    (2,  7), ( 4, 13), ( 5, 7), (10,  5), (13,  9), (15, 5),
    (17, 7), (19, 10), (22, 7), (25, 10), (29, 14), (30, 2)
]


""" sorts the particles with respect to their coordinates """
# sorts primarly with respect x and secondarily with respect y
Px = sorted( Ps, key = lambda t: (t[0], t[1]) )
# sorts primarly with respect y and secondarily with respect x
Py = sorted( Ps, key = lambda t: (t[1], t[0]) )


""" visualization of the particle positions """

# unpacks the particle positions into x, y coordinate arrays
P = np.array(Ps)
x, y = P.transpose()    # unpacking works for the transposed array

plt.close('all')        # closes all (existing) figures
plt.ion()               # enables interactive plotting
fig, ax = plt.subplots()# enables multiple plots on the same figure

# plots the particle positions in a 2D plot
ax.plot(x, y, linestyle="", marker="o", markersize=12, color="black")
ax.set_title('Points')
ax.set_xlim([1, 31])
ax.set_ylim([1, 15])


""" divides the system in half (left and right) """

# constructs Lx and Rx
Lx = Px[ 0 : ceil( len(Ps) // 2 ) ]         # selects particles in the left
Rx = Px[ ceil( len(Ps) // 2 ) : len(Ps) ]   # selects those in the right

""" plots the points sorted with respect to their x-coordinate """
fig, ax = plt.subplots()


# unpacks the particle coordinates on the left half for plotting
L = np.array(Lx)
X, Y = L.transpose()
ax.plot(X, Y, linestyle="", marker="o", color="blue", markersize=12)


# unpacks the particle coordinates on the right half for plotting
R = np.array(Rx)
X, Y = R.transpose()
ax.plot(X, Y, linestyle="", marker="o", color="red", markersize=12)
# sets the axes limits and the title of the figure
ax.set_xlim([1, 31])
ax.set_ylim([1, 15])
ax.set_title('Left and Right Halves')


# plots the Vertical line that divides the system in halves
middle = np.median(x)   # finds the middle value along the x axis

Vx = middle * np.ones(256)      # constant array of 256 elements
Vy = np.linspace(0, 40, 256)    # linear space of 256 elements
ax.plot(Vx, Vy, linestyle="--", color="black")


"""
divides horizontally to obtain four Cartesian quadrants
"""
# sorts particles on the left and right halves by their y coordinates
Ly = sorted(Lx, key = lambda t: (t[1], t[0]))
Ry = sorted(Rx, key = lambda t: (t[1], t[0]))


# left top and bottom (or Cartesian II and III quadrants, respectively)
leftBot_y = Ly[ 0 : ceil( len(Ly) // 2 ) ]
leftTop_y = Ly[ ceil( len(Ly) // 2 ) : len(Ly) ]


# right top and bottom (or Cartesian IV and I quadrants, respectively)
rightBot_y = Ry[ 0 : ceil( len(Ry) // 2 ) ]
rightTop_y = Ry[ ceil( len(Ry) // 2 ) : len(Ry) ]


""" plots the points sorted by their positions into quadrants """
fig, ax = plt.subplots()

# renders the vertical and horizontal lines that divide the system

vertical   = np.median( np.array(Ps)[:, 0] ) * np.ones(256) # middle x
horizontal = np.median( np.array(Ps)[:, 1] ) * np.ones(256) # middle y

x = np.linspace(0, 40, 256)
# note that the lines (x values) exceed the box dimensions on purpose
ax.plot(vertical, x, linestyle="--", color='black')
ax.plot(x, horizontal, linestyle="--", color='black')


# unpacks the particle positions on left bottom (quadrant III) for plotting
x, y = np.array(leftBot_y).transpose()
ax.plot(x, y, linestyle="", marker="o", color="blue", markersize=12)


# unpacks the particle positions on left top (quadrant II) for plotting
x, y = np.array(leftTop_y).transpose()
ax.plot(x, y, linestyle="", marker="*", color="blue", markersize=12)


# unpacks the positions on right bottom (quadrant IV) for plotting
x, y = np.array(rightBot_y).transpose()
ax.plot(x, y, linestyle="", marker="o", color="red", markersize=12)


# unpacks the positions on right top (quadrant I) for plotting
x, y = np.array(rightTop_y).transpose()
ax.plot(x, y, linestyle="", marker="*", color="red", markersize=12)


# sets the axes limits and the title of the figure
ax.set_xlim([1, 31])
ax.set_ylim([1, 15])
ax.set_title('Quadrants Partitioning')
