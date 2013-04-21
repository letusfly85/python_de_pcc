# -*- coding: utf-8 -*-

Num = 4
Wei = 5

W = [2, 1, 3, 2]
V = [3, 2, 4, 2]

w = len(W)
v = len(V)

ANCHOR = 9999999999
memsets = {}

def initialize_memsets():
    for i in range(0, w * v + 1):
        memsets[i] = {}
        for j in range(0, w * v + 1):
            memsets[i][j] = ANCHOR

    memsets[0][0] = 0

def solve():
    for i in range(0, Num):
        for j in range(0, w * v):
            if (j < V[i]):
                memsets[i+1][j] = memsets[i][j]
            else:
                memsets[i+1][j] = min(memsets[i][j], memsets[i][j-V[i]] + W[i])

    res = 0
    for i in range(0, w * v):
        if (memsets[Num][i] <= Wei):
            res = i

    print res

def __main__():
    initialize_memsets()
    solve()

__main__()
