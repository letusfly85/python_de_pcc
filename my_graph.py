# -*- coding: utf-8 -*-

class MyGraph:
    def __init__(self, n, c):
        self.node      = n
        self.color     = c
        self.neighbors = []

    def set_neighbor(self, n):
        self.neighbors.append(n)
