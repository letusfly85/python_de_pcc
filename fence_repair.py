# -*- coding: utf-8 -*-

def swap(a, b):
    x = a
    a = b
    b = x

def solve(num, boards):
    ans = 0

    while (num > 1):
        min1 = 0
        min2 = 1
        if (boards[min1] > boards[min2]):
            swap(min1, min2)

        for idx in range(2, num - 1):
            if (boards[idx] < boards[min1]):
                min2 = min1
                min1 = idx

            elif (boards[idx] < boards[min2]):
                min2 = idx

        t = boards[min1] + boards[min2]
        ans += t

        if (min1 == num -1):
            swap(min1, min2)

        boards[min1] = t
        boards[min2] = boards[num -1]
        num -= 1

    print ans

def __main__():
    N = 3
    BOARDS = [8, 5, 8]

    solve(N, BOARDS)

__main__()


