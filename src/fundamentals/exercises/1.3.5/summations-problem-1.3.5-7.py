#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Algorithms and Complexity                                 February 05, 2022
IST 4310
Prof. M Diaz-Maldonado


Synopsis:
Solves problems 1.3.5-7a, 1.3.5-7e, and 1.3.5-7f.


Copyright (c) 2022 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] JJ McConnell, Analysis of Algorithms, 2nd edition, 2007.
"""


from numpy import arange


N = 16              # end-value of the summation
n = arange(1, N+1)  # creates a sequence in the asymmetric range [1, N+1)
s = 3*n+7           # generates the summation sequence

ans = (
    f'\nproblem  1.3.5-7a:\n'
    f'exact:   {3 * ( N*(N+1)/2 ) + 7*N}\n'
    f'numeric: {s.sum()}\n'
)

print(ans)


"""
Applies equation (1.18) to obtain the summation.
"""
N = 15              # end-value of the summation
n = arange(0, N+1)  # creates a sequence in the asymmetric range [0, N+1)
A = 2
s = A**n            # generates the summation sequence

ans = (
    f'\nequation (1.18):\n'
    f'exact:   {( (A**(N+1) - 1) / (A - 1) )}\n'    # eqtn (1.18)
    f'numeric: {s.sum()}\n'
)

print(ans)



"""
problem 1.3.5-7e
for n=[1, N], calculate the sum(6^n)
"""

A = 6
N = 15
n = arange(1, N+1)
s = A**n

ans = (
    f'\nproblem 1.3.5-7e:\n'
    f'exact:   {( (A**(N+1) - 1) / (A - 1) - 1 )}\n'
    f'numeric: {s.sum()}\n'
)

print(ans)



"""
problem 1.3.5-7f
for n=[7, N], calculate the sum(4^n)
"""

A = 4
N = 15
n = arange(7, N+1)
s = A**n

exact = (A**(N+1) - 1) / (A - 1) - (A**7 - 1) / (A - 1)

ans = (
    f'\nproblem 1.3.5-7f:\n'
    f'exact:   {exact}\n'
    f'numeric: {s.sum()}\n'
)

print(ans)
