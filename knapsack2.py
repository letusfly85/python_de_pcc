# -*- coding: utf-8 -*-

Num = 4
Wei = 5

V = [3, 2, 4, 2]
W = [2, 1, 3, 4]

memsets = {}

def initialize_memsets():
    for i in range(0, 100):
        memsets[i] = {}

def register_memsets(i, j, res):

    if (memsets.has_key(i) == True): 
        memsets[i] = {}

    memsets[i][j] = res

def rec(i, j):
    if (memsets[i].has_key(j) != False):
        return memsets[i][j]

    res = 0
    if (i == Num):
        res = 0

    elif (j < W[i]):
        res = rec(i + 1, j)

    else:
        left  = rec(i + 1, j)
        right = rec(i + 1, j - W[i]) + V[i]
        res = max(left, right)

    register_memsets(i, j, res)
    return res

def solve():
    print rec(0, Wei)


def __main__():
    initialize_memsets()
    solve()

__main__()
