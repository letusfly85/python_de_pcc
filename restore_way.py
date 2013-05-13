# -*- coding: utf-8 -*-

import my_graph

ANCHOR  = 999999999999
V       = 7
memsets = {}
used    = {}
prev    = {}
edges   = []
nodes   = []

def generate_edges():
    a  = my_graph.MyGraph(0, 0)
    b  = my_graph.MyGraph(1, 0)
    c  = my_graph.MyGraph(2, 0)
    d  = my_graph.MyGraph(3, 0)
    e  = my_graph.MyGraph(4, 0)
    f  = my_graph.MyGraph(5, 0)
    g  = my_graph.MyGraph(6, 0)

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

def cost(u, v):
    nf = nodes[u]
    nt = nodes[v]

    for i in range(0, len(edges)):
        e = edges[i]
        if (e.node_from.node == nf.node and e.node_to.node == nt.node):
            return e.cost
    
    return ANCHOR

def initialize_memsets():
    for i in range(0, V):
        memsets[i] = ANCHOR
        used[i]    = False
        prev[i]    = -1

def dijkstra():
    initialize_memsets()
    memsets[0] = 0

    while (True):
        v = -1
        for u in range(0, V):
            if (used[u] == False and (v == -1 or memsets[u] < memsets[v])):
                v = u

        if (v == -1):
            break

        used[v] = True

        for u in range(0, V):
            if (memsets[u] > memsets[v] + cost(v, u)):
                memsets[u] = memsets[v] + cost(v, u)
                prev[u] = v

def get_path(t):
    path = []

    i = t
    while (True):
        if (prev[i] == -1):
            return path[::-1]

        path.append(prev[i])
        i = prev[i]

    return path[::-1]

def __main__():
    generate_edges()
    dijkstra()
    print get_path(V-1)

__main__()
