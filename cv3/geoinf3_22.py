#Graph definition
import operator
from operator import *
from math import *

#Nodes
U = [1, 2, 3, 4, 5, 6, 7, 8, 9]
H = [
    [1, 2, 8],
    [1, 3, 4],
    [1, 5, 2],
    [2, 1, 8],
    [2, 3, 5],
    [2, 4, 2],
    [2, 7, 6],
    [2, 8, 7],
    [3, 1, 4],
    [3, 2, 5],
    [3, 6, 3],
    [3, 7, 4],
    [4, 2, 2],
    [4, 9, 3],
    [5, 1, 2],
    [5, 6, 5],
    [6, 3, 3],
    [6, 5, 5],
    [6, 7, 5],
    [6, 8, 7],
    [6, 9, 10],
    [7, 2, 6],
    [7, 3, 4],
    [7, 6, 5],
    [7, 8, 3],
    [8, 2, 7],
    [8, 6, 7],
    [8, 7, 3],
    [8, 9, 1],
    [9, 4, 3],
    [9, 6, 10],
    [9, 8, 1]
    ]

def mst (U,H):
    T = []
    wt = 0
    p = [-1]*(len(U)+1)
    r = [inf] * (len(U) + 1)

    #Make set
    for u in U:
        p[u] = u
        r[u] = 0

    #Sort edges according to w
    HS = sorted(H, key=itemgetter(2))

    # Proccess edges according to w
    for h in HS:
        u, v, w = h

        #Nodes are in different trees
        if findpc(u, p) != findpc(v, p):
            #Merge two subtrees
            union(u, v, p)

            #Add edge to spanning tree
            T.append(h)

            #Weight increment
            wt += w

    return T, wt

#Find root (no compression)
def find (u, p):
    while (p[u] != u):
        u = p[u]

    return u

def findpc (u, p):
    #find root
    root = find(u,p)

    # reconnect nodes to root
    while u != root:
        #Store parent
        pu = p[u]


        #Reconnect u to root
        p[u] = root

        #Continue from parent
        u = pu

    return root

#union of two subtrees
def union (u, v, p):
    root_u = findpc(u, p)
    root_v = findpc (v, p)

    #Merge two subtrees
    p[root_u] = root_v

def wunion (u, v, p, r):
    root_u = findpc(u, p)
    root_v = findpc (v, p)

    #Merge two subtrees
    if r[root_u] > r[root_v]:
        p[root_v] = root_u
    elif r[root_v] > r[root_u]:
        p[root_u] = root_v
    else:
        p[root_v] = root_u
        r[root_u] +=1


tree, tree_weight = mst(U, H)
print(tree, tree_weight)