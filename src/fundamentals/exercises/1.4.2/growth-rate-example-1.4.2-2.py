#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Algorithms and Complexity                                 February 16, 2022
IST 4310
Prof. M Diaz-Maldonado


Synopsis:
Plots f(n) and g(n) to verify that g(n) = O(f). It also plots f(n) and its
asymptotic approximation F(n) on the same loglog plot to show that these
are the same as `n' grows towards infinity.


Sinopsis:
Grafica las funciones f(n) y g(n) para verificar que g(n) = O(f). Tambien
grafica f(n) y su aproximacion asintotica F(n) en la misma figura en
escala logaritmica para demostrar que estas son las mismas a medida que
`n' crece hacia el infinito.


Copyright (c) 2022 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] JJ McConnell, Analysis of Algorithms, 2nd edition, 2007.
"""


from numpy import log2
from numpy import sqrt
from numpy import arange
from numpy import logspace
from scipy.special import factorial
import matplotlib as mpl
mpl.use('qt5agg')
mpl.rcParams['text.usetex'] = True
from matplotlib import pyplot as plt


n = arange(1, 156)
f = n + sqrt(n) * log2( factorial(n) )
g = n + n * log2(n)

N = logspace(0, 3)
G = N + N * log2(N)
F = N + N * sqrt(N) * log2(N)


plt.close('all')
plt.ion()
fig, ax = plt.subplots()
ax.plot(n, g/f, linestyle='-',  color='red',
    label=r'exact: $ g(n) / f(n) $')
ax.plot(N, G/F, linestyle='--', color='blue',
    label=r'approximate: $ G(n) / F(n) $')
ax.set_xlabel(r'$n$')
ax.legend()


fig, ax = plt.subplots()
ax.loglog(n, g/f, linestyle='-',  color='red',
    label=r'exact: $ g(n) / f(n) $')
ax.loglog(N, G/F, linestyle='--', color='blue',
    label=r'approximate: $ G(n) / F(n) $')
ax.set_xlabel(r'$n$')
ax.legend()


"""
Figure shows that the asymptotic behavior of f(n) and its approximation,
F(n), is the same. (Note: Respective slopes are the same.)
"""
fig, ax = plt.subplots()
ax.loglog(n, g, linestyle='-.', color='blue',  label=r'$ g(n) $')
ax.loglog(n, f, linestyle='-',  color='black', label=r'$ f(n) $')
ax.loglog(N, F, linestyle='--', color='black', label=r'$ F(n) $')
ax.set_xlabel(r'$n$')
ax.legend(loc='upper left')
