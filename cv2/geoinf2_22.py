import queue
import math
from math import inf

#Graph definition
G = {
    1 : {2:8, 3:4, 5:2},
    2 : {1:8, 3:5, 4:2, 7:6, 8:7},
    3 : {1:4, 2:5, 6:3, 7:4},
    4 : {2:2, 9:3},
    5 : {1:2, 6:5},
    6 : {3:3, 5:5, 7:5, 8:7, 9:10},
    7 : {2:6, 3:4, 6:5, 8:3},
    8 : {2:7, 6:7, 7:3, 9:1},
    9 : {4:3, 6:10, 8:1}
}

def dijkstra(G, s, e):
    #find shortest path between two nodes
    p = [-1]*(len(G)+1)
    d = [inf]*(len(G)+1)

    #inicialization of distance
    d[s]= 0

    #Priority queue
    Q = queue.PriorityQueue()

    #Add start note
    Q.put((0,s))

    #Repeat until priority queue is empty
    while not Q.empty():
        #Node with minimum distance
        du, u = Q.get()

        #Browse adjacent nodes
        for v, wuv in G[u].items():

            #Relaxation of uv
            if d[v] > d[u]+wuv:
                d[v] = d[u]+wuv
                p[v] = u
                Q.put ((d[v], v))
    return p, d


def pathReconstruction (p, s, e):
    #Backward path reconstruction
    path = []
    while e != s:
        path.append(e)
        e = p[e]
    return path


p,d = dijkstra(G, 1, 9)
path = pathReconstruction(p, 1,  9)
print (path)