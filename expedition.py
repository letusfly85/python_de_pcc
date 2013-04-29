# -*- coding: utf-8 -*-

from   heapq import heappush, heappop

global N
global L

N = 4
L = 25

P = 10

A = [10, 14, 20, 21]
B = [10, 5,  2,  4]

def initialize():
    A.append(L)
    B.append(0)
    N = 5

    pos  = 0
    tank = P
    ans  = 0

    heap = []

    for i in range(0, N):
        d = A[i] - pos

        while (tank-d < 0):
            if (len(heap) == 0):
                print "-1"
                return

            tank += heappop(heap)
            ans += 1

        tank -= d
        pos  =  A[i]
        heap.append(B[i])
        heap.sort

    print ans

def __main__():
    initialize()

__main__()
