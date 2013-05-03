# -*- coding: utf-8 -*-

color = {}
for k in range(0, 100):
    if (k % 2 == 0):
        color[k] = -1
    else:
        color[k] = 1

class MyGraph:
    def __init__(self, n, c):
        self.node      = n
        self.color     = c
        self.neighbors = []

    def set_neighbor(self, n):
        self.neighbors.append(n)

def generate_graphs():
    # グラフを生成する

    # グラフの頂点を決定する
    g0 = MyGraph(1, 0)
    g1 = MyGraph(2, 0)
    g2 = MyGraph(3, 0)
    g3 = MyGraph(4, 0)
    g4 = MyGraph(5, 0)

    # 隣接するグラフを各頂点にセットする
    g0.set_neighbor(g1)
    g0.set_neighbor(g2)

    g1.set_neighbor(g0)
    g1.set_neighbor(g2)

    g2.set_neighbor(g0)
    g2.set_neighbor(g1)

    graphs = [g0, g1, g2]

    return graphs


def dfs(G, v, c):
    G[v].color = c

    for i in range(0, k):
        if (G[v].neighbors[i].color == c):
            return False

        if (G[v].neighbors[i].color == 0 and dfs(G, G[v].neighbors[i].node, -c) == False):
            return False

    return True

def solve():
    G = generate_graphs()

    for i in range(0, len(G)):
        if (color[i] == 0):
            if (dfs(G, i, 1) == False):
                print "None"

    print "Yes"

def __main__():
    solve()

__main__()
