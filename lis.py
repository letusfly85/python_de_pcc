# -*- coding: utf-8 -*-

Num = 5
A   = [4, 2, 3, 1, 5]

memsets = {}

def initialize_memsets():
    memsets[0] = 0

def solve():
    for i in range(0, Num):
        memsets[i+1] = 1
        
        for j in range(0, i):
            if (A[j] < A[i]):
                memsets[i+1] = max(memsets[i+1], memsets[j]+1)

    print memsets[Num]

def __main__():
    initialize_memsets()
    solve()

__main__()
