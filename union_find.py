# -*- coding: utf-8 -*-

class UnionFind:

    def __init__(self, n):
        self.par  = []
        self.rank = []

        for i in range(0, n):
            self.par.append(i)
            self.rank.append(i)

    def find(self, x):
        if (self.par[x] == x):
            return x
        else:
            buf = find(self.par[x])
            return buf

    def unite(self, x, y):
        x = find(x)
        y = find(y)

        if (x == y):
            return

        if (rank[x] < rank[y]):
            self.par[x] = y
        else:
            self.par[y] = x
            if (rank[x] == rank[y]):
                rank[x] += 1

    def same(x, y):
        return (find(x) == find(y))
