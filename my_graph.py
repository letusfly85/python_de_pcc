# -*- coding: utf-8 -*-

class MyGraph:
    def __init__(self, n, c):
        self.node      = n
        self.color     = c
        self.neighbors = []

    def set_neighbor(self, n):
        self.neighbors.append(n)

    def set_neighbors(self, ns):
        for i in range(0, len(ns)):
            self.set_neighbor(ns[i])

    def who_am_i(self, n, ns):
        for i in range(0, len(ns)):
            if (n == ns[i].node):
                return ns[i]

class MyEdge:
    def __init__(self, nf, nt, c):
        self.node_from = nf 
        self.node_to   = nt
        self.cost      = c


class MyPair:
    def __init__(self, sd, n):
        self.shortest_distance = sd
        self.node              = n
