# -*- coding: utf-8 -*-

Num = 3
Key = 17

A = [3, 5, 8]
M = [3, 2, 2]

ANCHOR = -1
memsets = {}

def initialize_memsets():
    for j in range(0, Key + 1):
        memsets[j] = ANCHOR

def solve():
    chance = 0

    memsets[0] = 0
    for i in range(0, Num):
        for j in range(0, Key + 1):
            if (memsets[j] >= 0):
                memsets[j] = M[i]
            elif (j < A[i] or memsets[j-A[i]] <= 0):
                memsets[j] = ANCHOR
            else:
                memsets[j] = memsets[j-A[i]] -1

    if (memsets[Key] >= 0):
        print "It's possible"
    else:
        print "It's impossible"

def __main__():
    initialize_memsets()
    solve()

__main__()
