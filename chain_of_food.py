# -*- coding: utf-8 -*-

import union_find


N  = 100
K  = 7

T  = [1,   2, 2, 2, 1, 2, 1]
X  = [101, 1, 2, 3, 1, 3, 5]
Y  = [1,   2, 3, 3, 3, 1, 5]

def solve():
    uf = union_find.UnionFind(N * 3)

    ans = 0
    for i in range(0, K):
        t = T[i]
        x = X[i] - 1
        y = Y[i] - 1
        
        if (x < 0 or N <= x or y < 0 or N <= y):
            ans += 1
            continue

        if (t == 1):
                if (uf.same(x, y + N) or uf.same(x, y + 2 * N)):
                    ans += 1
                else:
                    uf.unite(x, y)
                    uf.unite(x + N, y + N)
                    uf.unite(x + N * 2, y + N * 2)

        else:
            if (uf.same(x, y) or uf.same(x, y + 2 * N)):
                ans += 1
            else:
                uf.unite(x, y + N)
                uf.unite(x + N, y + 2 * N)
                uf.unite(x + 2 * N, y)

    print ans

def __main__():
    solve()

__main__()

        
