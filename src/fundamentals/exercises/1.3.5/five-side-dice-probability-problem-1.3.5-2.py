#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Algorithms and Complexity                                 February 05, 2022
IST 4310
Prof. M Diaz-Maldonado


Synopsis:
Uses a Binary Search Tree BST to solve the five-side dice problem 1.3.5-2.
Generates a table of possible outcomes (total of the dice pair) and their
respective probabilities.


Copyright (c) 2022 Misael Diaz-Maldonado
This file is released under the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


References:
[0] JJ McConnell, Analysis of Algorithms, 2nd edition, 2007.
[1] trees: docs.python.org/3/library/stdtypes.html#mapping-types-dict
"""


from numpy import array


n = 0
tree = {}
# initializes binary search tree with zeroes
for i in range(1, 6):
    for j in range(1, 6):
        tree[i+j] = 0
        n += 1


# counts number of outcome (the dice pair total) instances
for i in range(1, 6):
    for j in range(1, 6):
        tree[i+j] += 1


""" output """

# prints table of results
header = (
    '\n\nProblem 1.3.5-2: Five-side Dice Probability Problem\n\n'
    'outcome    repetitions    probability\n'
    '-------------------------------------'
)
print(header)
for (key, val) in tree.items():
    print(f'{key:4d}        {val:4d}          {val/n:8.2f}')


""" post-processing """


# verifies that the total probability is one
p = array( list( tree.values() ) ).sum() / n
print(f'\n\ntotal probability: {p}\n\n')
