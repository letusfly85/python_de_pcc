# -*- coding: utf-8 -*-

Wei = 5
Num = 4

W = [2, 1, 3, 4]
V = [3, 2, 4, 2]

def rec(i, j):
    res = 0

    if (i == Num):
        res = 0

    elif (j < W[i]):
        res = rec(i + 1, j)

    else:
        res = max(rec(i + 1, j), rec(i + 1, j - W[i]) + V[i])

    return res

def solve():
    print rec(0, Wei)


def __main__():
    solve()

__main__()
