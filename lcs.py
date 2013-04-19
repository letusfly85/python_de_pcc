# -*- coding: utf-8 -*-

N = 4
M = 4

STR1 = "abcd"
STR2 = "becd"

memsets    = {}

def initialize_memsets():
    for i in range(0, 10):
        memsets[i] = {}
        for j in range(0, 10):
            memsets[i][j] = 0

def solve(target_str):
    for i in range(0, N):
        for j in range(0, M):
            if (STR1[i] == STR2[j]):
                memsets[i+1][j+1] = memsets[i][j] + 1
                target_str += STR1[i]
                
            else:
                memsets[i+1][j+1] = max(memsets[i][j+1], memsets[i+1][j])

    print memsets[N][M]
    print target_str

def __main__():
    initialize_memsets()
    target_str = ""
    solve(target_str)

__main__()
