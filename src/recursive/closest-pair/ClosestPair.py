#!/usr/bin/env python3
# -*- coding: utf-8 -*-
syn="""
Algorithms and Complexity                                 February 20, 2022
IST 3498
Prof. M Diaz-Maldonado

Synopsis:
Divide and Conquer Algorithms. Closest Pair Problem. Partitions the
particles into quadrants and plots their coordinates in a 2D plot and
finds the closest pair via the Brute Force and Divide and Conquer
Algorithms.


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
# imports ticker for setting the location of the plot ticks
from matplotlib import ticker


def distance(P):
    """
    Synopsis:
    Finds the distance of the closest pair.

    Input:
    P       sorted list of a tuple of (x, y) coordinates

    Output:
    ith     coordinates of the ith particle of the closest pair
    jth     coordinates of the jth particle of the closest pair
    d_min   distance of the closest pair
    """

    # initializes the min (squared) distance with the maximum one
    xi, yi = (P[0][0], P[0][1])
    xj, yj = (P[ len(P) - 1 ][0], P[ len(P) - 1 ][1])
    d_max = (xi - xj)**2 + (yi - yj)**2

    d_min = d_max
    ith, jth = (0, 0)
    for i in range( len(P) - 1 ):
        for j in range (i + 1, len(P)):
            # calculates the relative particle distance N * (N - 1)/2 times

            # unpacks the coordinates of the ith and jth particles
            xi, yi = (P[i][0], P[i][1])
            xj, yj = (P[j][0], P[j][1])

            # calculates their (squared) distance
            d = (xi - xj)**2 + (yi - yj)**2

            if (d < d_min):
                ith = i
                jth = j
                d_min = d

    return ( P[ith], P[jth], np.sqrt(d_min) )


print(syn)


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



""" divides the particles into quadrants """

# constructs Lx and Rx
Lx = Px[ 0 : ceil( len(Ps) // 2 ) ]         # selects particles in the left
Rx = Px[ ceil( len(Ps) // 2 ) : len(Ps) ]   # selects those in the right

# constructs Ly and Ry
Ly = sorted(Lx, key = lambda t: (t[1], t[0]))
Ry = sorted(Rx, key = lambda t: (t[1], t[0]))


""" plots the points sorted by their positions into quadrants """

plt.close('all')
plt.ion()
fig, ax = plt.subplots()

# renders the vertical and horizontal lines that divide the system

vertical   = np.median( np.array(Ps)[:, 0] ) * np.ones(256) # middle x
horizontal = np.median( np.array(Ps)[:, 1] ) * np.ones(256) # middle y

x = np.linspace(0, 40, 256)
# note that the lines (x values) exceed the box dimensions on purpose
ax.plot(vertical, x, linestyle="--", color='black')
ax.plot(x, horizontal, linestyle="--", color='black')

x, y = np.array( Ly[ 0 : ceil(len(Ly)//2) ] ).transpose()
ax.plot(x, y, linestyle="", marker="o", color="blue", markersize=12)

x, y = np.array( Ly[ ceil(len(Ly)//2) : len(Ly) ] ).transpose()
ax.plot(x, y, linestyle="", marker="*", color="blue", markersize=12)

x, y = np.array( Ry[ 0 : ceil(len(Ry)//2) ] ).transpose()
ax.plot(x, y, linestyle="", marker="o", color="red", markersize=12)

x, y = np.array( Ry[ ceil(len(Ry)//2) : len(Ry) ] ).transpose()
ax.plot(x, y, linestyle="", marker="*", color="red", markersize=12)


# places major ticks every two units on the x, y axes
ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_major_locator(ticker.MultipleLocator(2))

# sets the axes limits and the title of the figure
ax.set_xlim([np.array(Ps)[:, 0].min() - 1, np.array(Ps)[:, 0].max() + 1])
ax.set_ylim([np.array(Ps)[:, 1].min() - 1, np.array(Ps)[:, 1].max() + 1])
ax.set_title('Quadrants Partitioning')



""" Divide and Conquer Algorithm """
# applies the Brute Force Algorithm on the (three particle) quadrants
il_1, jl_1, dl_1 = distance(Ly[ 0 : ceil(len(Ly)//2) ])
il_2, jl_2, dl_2 = distance(Ly[ ceil(len(Ly)//2) : len(Ly) ])
ir_1, jr_1, dr_1 = distance(Ry[ 0 : ceil(len(Ry)//2) ])
ir_2, jr_2, dr_2 = distance(Ry[ ceil(len(Ry)//2) : len(Ry) ])


"""
finds the closest pair on the left half (quadrants II and III)
and obtains the indexes i, j with respect to the (original) list Ps
"""
if (dl_1 < dl_2):
    il, jl = (il_1, jl_1)
    dl = dl_1
else:
    il, jl = (il_2, jl_2)
    dl = dl_2


# finds the closest pair on the right half (quadrants I and IV)
if (dr_1 < dr_2):
    ir, jr = (ir_1, jr_1)
    dr = dr_1
else:
    ir, jr = (ir_2, jr_2)
    dr = dr_2


# finds which half (Left or Right) has the closest pair
if (dl < dr):
    i, j = (il, jl)
    ds = dl
else:
    i, j = (ir, jr)
    ds = dr


"""
checks if the closest pair is actually near the quadrant divisions
"""

# constructs My
"""
Note:
the min and max functions are used to avert exceeding the bounds of the
lists Px and Py. The referenced particles are potentially within the
smallest distance, ds, found thus far.
"""
My = Py[ max( 0, ceil(len(Py)//2) - ceil(ds/2) ) :
         min( len(Py), ceil(len(Py)//2) + ceil(ds/2) ) ]
im, jm, dm = distance(My)


if (dm < ds):
    i, j = (im, jm)
    ds = dm



# constructs Mx
Mx = Px[ max( 0, ceil(len(Px)//2) - ceil(ds/2) ) :
         min( len(Px), ceil(len(Px)//2) + ceil(ds/2) ) ]
im, jm, dm = distance(Mx)


if (dm < ds):
    i, j = (im, jm)
    ds = dm


""" Shows Divide and Conquer Algorithm Solution """

out = (
    f'\nDivide and Conquer Algorithm:\n'
    f'minimum distance: {ds}\n'
    f'coordinates of closest pair: {i}, {j}\n'
)

print(out)


""" applies the Brute Force Algorithm on all the particles """
Pi, Pj, d_min = distance(Px)

out = (
    f'\nBrute Force Algorithm:\n'
    f'minimum distance: {d_min}\n'
    f'coordinates of closest pair: {Pi}, {Pj}\n'
)

print(out)
