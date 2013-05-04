# -*- coding: utf-8 -*-

import my_edge

ANCHOR  = 999999999999
memsets = {}
edges   = []

def generate_edges():
    ab = my_edge.MyEdge(0,   1,  2)
    ac = my_edge.MyEdge(0,  -1,  5)
    bc = my_edge.MyEdge(1,  -1,  4)
    bd = my_edge.MyEdge(1,  -2,  6)
    be = my_edge.MyEdge(1,   3,  10)
    cd = my_edge.MyEdge(-1, -2,  2)
    db = my_edge.MyEdge(-2,  2,  6)
    df = my_edge.MyEdge(-2, -3,  1)
    ef = my_edge.MyEdge(3,  -3,  3)
    eg = my_edge.MyEdge(3,   4,  5)
    fe = my_edge.MyEdge(-3,  3,  3)
    fg = my_edge.MyEdge(-3,  4,  9)

    edges.append(ab)
    edges.append(ac)
    edges.append(bc)
    edges.append(bd)
    edges.append(be)
    edges.append(cd)
    edges.append(db)
    edges.append(df)
    edges.append(ef)
    edges.append(eg)
    edges.append(fe)
    edges.append(fg)

def initialize_memsets():
    for i in range(-99, 100):
        memsets[i] = ANCHOR

def shortest_path(s):
    memsets[s] = 0
    E = len(edges)

    while (True):
        update = False

        for i in range(0, E):
            e = edges[i]

            if (memsets[e.from_pos] != ANCHOR and memsets[e.to_pos] > memsets[e.from_pos] + e.cost):
                memsets[e.to_pos] = memsets[e.from_pos] + e.cost
                update = True

        if update == False:
            break

    buf = 0
    for i in range(0, len(memsets)):
        if memsets[i] == ANCHOR:
            print buf
            break
        else:
            buf = memsets[i]

def solve():
    initialize_memsets()
    generate_edges()
    shortest_path(0)


def __main__():
    solve()

__main__()
