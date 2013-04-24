# -*- coding: utf-8 -*-

import bisect

Num = 5
A   = [4, 2, 3, 1, 5]

ANCHOR = 9999999999

memsets = []

def initialize_memsets():
    for i in range(0, Num):
        memsets.append(ANCHOR)

def solve():
    buf = 0
    for i in range(0, Num):
        idx =  bisect.bisect_left(memsets, A[i])
        if (memsets[i] > A[i]):
            memsets[idx] = A[i]
        
    res = bisect.bisect_left(memsets, ANCHOR)
    print res

def __main__():
    initialize_memsets()
    solve()

__main__()
