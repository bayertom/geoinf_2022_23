#Graph
G = {
    1 : [2, 3, 5],
    2 : [1, 3, 4, 7, 8],
    3 : [1, 2, 6, 7],
    4 : [2, 9],
    5 : [1, 6],
    6 : [3, 5, 7, 8, 9],
    7 : [2, 3, 6, 8],
    8 : [2, 6, 7, 9],
    9 : [4, 6, 8]
}

def BFS(G, u, P):
    S = ['N']*(len(G)+1)
    Q = []
    Q.append(u)
    S[u] ='O'
    while Q:
        u = Q.pop(0)
        for v in G[u]:
            if S[v] == 'N':
                S[v] = 'O'
                P[v] = u
                Q.append(v)
        S[u] = 'C'


def DFSR(G, S, P, u):
    S[u] = 'O'
    for v in G[u]:
        if S[v] == 'N':
            P[v] = u
            DFSR(G, S, P, v)
    S[u] = 'C'

def DFS(G, u, P):
    S = ['N']*(len(G)+1)
    DFSR(G, S, P, u)


