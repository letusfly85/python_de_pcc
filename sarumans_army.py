# -*- coding: utf-8 -*-

def solve(n, r, target):
    _target = []
    for entry in sorted(target):
        _target.append(entry)

    idx = 0
    ans = 0
    while (idx < len(target)):

        s = _target[idx]

        while (idx < len(target) and _target[idx] <= (s + r)):
            idx += 1

        p = _target[idx - 1]

        while (idx < len(target) and _target[idx] <= (p + r)):
            idx += 1

        ans += 1
            
    print ans

def __main__():
    N = 6
    R = 10
    TARGET = [7, 15, 1, 20, 30, 50]

    solve(N, R, TARGET)

__main__()
