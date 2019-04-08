#!/usr/bin/env python3

"""
Manhattan Tourist Problem2
Max Prem
./MaxPrem-Manhattantourist2.py < rmHVD_10_23
./MaxPrem-Manhattantourist2.py < rmHVD_999_23
results: rmHVD_10_23: 68.18; rmHVD_999_23: 7227.54
"""

import sys
from numpy import zeros


def MatrixReader(matrix):
    direction = []
    i = 0
    for line in matrix:
        if line.startswith(" "):
            temp = line.split()
            direction.append([])
            for number in temp:
                direction[i].append(float(number))
            i += 1
        if line.startswith("-"):
            break
    return direction


def MTP(matrix):


    down = MatrixReader(matrix)
    right = MatrixReader(matrix)
    dia = MatrixReader(matrix)

    matrix.close()

    n = len(down)
    m = len(right[0])
    s = zeros((n + 1, m + 1))

    # Compute the first row and column.
    for i in range(1, n + 1):
        s[i][0] = round((s[i - 1][0] + down[i - 1][0]), 2)
    for j in range(1, m + 1):
        s[0][j] = round((s[0][j - 1] + right[0][j - 1]), 2)

    # Compute the interior values.
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            s[i][j] = round(max(s[i - 1][j] + down[i - 1][j], s[i][j - 1] + right[i][j - 1],
                          s[i - 1][j - 1] + dia[i - 1][j - 1]), 2)

    return s[n][m]


matrix = sys.stdin
score = MTP(matrix)
print(score)
