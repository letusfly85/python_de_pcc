# -*- coding: utf-8 -*-

Num = 3
Wei = 7

W = [3, 4, 2]
V = [4, 5, 3]

memsets = {}

def initialize_memsets():
    for i in range(0, 10):
        memsets[i] = {}
        for j in range(0, 10):
            memsets[i][j] = 0

def solve():
    for i in range(0, Num):
        for j in range(0, Wei+1):

            if (j < W[i]):
                memsets[i+1][j] = memsets[i][j]
            else:
                memsets[i+1][j] = max(memsets[i][j], memsets[i+1][j-W[i]] + V[i])
            
    print memsets[Num][Wei]

def __main__():
    initialize_memsets()
    solve()

__main__()
