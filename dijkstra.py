# -*- coding: utf-8 -*-

import my_graph

ANCHOR  = 999999999999
V       = 7
memsets = {}
used    = {}
edges   = []
nodes   = []

def generate_edges():
    a  = my_graph.MyGraph(1, 0)
    b  = my_graph.MyGraph(2, 0)
    c  = my_graph.MyGraph(3, 0)
    d  = my_graph.MyGraph(4, 0)
    e  = my_graph.MyGraph(5, 0)
    f  = my_graph.MyGraph(6, 0)
    g  = my_graph.MyGraph(7, 0)

    a.set_neighbors([b, c])
    b.set_neighbors([a, c, d, e])
    c.set_neighbors([a, b, d])
    d.set_neighbors([b, c, f])
    e.set_neighbors([b, f, g])
    f.set_neighbors([d, e, g])
    g.set_neighbors([e, f])

    nodes.append(a)
    nodes.append(b)
    nodes.append(c)
    nodes.append(d)
    nodes.append(e)
    nodes.append(f)
    nodes.append(g)

    ab = my_graph.MyEdge(a, b, 2)
    ac = my_graph.MyEdge(a, c, 5)
    bc = my_graph.MyEdge(b, c, 4)
    bd = my_graph.MyEdge(b, d, 6)
    be = my_graph.MyEdge(b, e, 10)
    cd = my_graph.MyEdge(c, d, 2)
    db = my_graph.MyEdge(d, b, 6)
    df = my_graph.MyEdge(d, f, 1)
    ef = my_graph.MyEdge(e, f, 3)
    eg = my_graph.MyEdge(e, g, 5)
    fe = my_graph.MyEdge(f, e, 3)
    fg = my_graph.MyEdge(f, g, 9)

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
    for i in range(-1, len(nodes)):
        memsets[i] = ANCHOR
        used[i]    = False

def cost(u, v):
    nf = nodes[u]
    nt = nodes[v]

    for i in range(0, len(edges)):
        e = edges[i]
        if (e.node_from.node == nf.node and e.node_to.node == nt.node):
            return e.cost
    
    return ANCHOR

def dijkstra():
    memsets[0] = 0

    while (True):
        v = -1

        for i in range(0, len(nodes)):
            if (used[i] == False and (v == -1 or memsets[i] < memsets[v])):
                v = i

        if (v == -1):
            break

        used[v] = True

        for k in range(0, len(nodes)):
            memsets[k] = min(memsets[k], memsets[v] + cost(v, k))

    print memsets[len(nodes) -1]

def solve():
    generate_edges()
    initialize_memsets()
    dijkstra()


def __main__():
    solve()

__main__()
