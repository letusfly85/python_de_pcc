# -*- coding: utf-8 -*-


def solve(target_str):
    a = 0
    b = len(target_str) - 1
    ary = list(target_str)

    while (a <= b):
        left = False
        for idx in range(0, b-a):
            if (ary[a + idx]   < ary[b - idx]):
                left = True
                break
            elif (ary[a + idx] > ary[b - idx]):
                left = False
                break

        if (left):
            print ary[a]
            a += 1
        else:
            print ary[b]
            b -= 1

def __main__():
    TARGET_STR = "ACDBCB"
    solve(TARGET_STR)

__main__()
