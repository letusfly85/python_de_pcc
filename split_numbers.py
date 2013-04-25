# -*- coding: utf-8 -*-

import bisect

N = 4
M = 3
TARGET = 10000

memsets = {}

def initialize_memsets():
    for i in range(0, M+1):
        memsets[i] = {}

        for j in range(0, N+1):
            memsets[i][j] = 0

    memsets[0][0] = 1

def solve():
    for i in range(1, M+1):
        for j in range(0, N+1):
            if (j-i >= 0):
                memsets[i][j] = (memsets[i-1][j] + memsets[i][j-1]) % TARGET
            else:
                memsets[i][j] = memsets[i-1][j]

    print memsets[M-1][N-1]

def __main__():
    initialize_memsets()
    solve()

__main__()
