# -*- coding: utf-8 -*-

N = 3
M = 3
A = [1, 2, 3]
ANCHOR = 10000

memsets = {}

def initialize_memsets():
    for i in range(0, M+1):
        memsets[i] = {}

        for j in range(0, N+1):
            if j == 0:
                memsets[i][j] = 1
            else:
                memsets[i][j] = 0

def solve():
    for i in range(0, N):
        for j in range(1, M+1):
            if (j - 1 - A[i] >= 0):
                memsets[i+1][j] = (memsets[i+1][j-1] + memsets[i][j] - memsets[i][j-1-A[i]]) % ANCHOR
            else:
                memsets[i+1][j] = (memsets[i+1][j-1] + memsets[i][j]) % ANCHOR

    print memsets[M][N]

def __main__():
    initialize_memsets()
    solve()

__main__()
