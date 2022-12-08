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

def BFS(G, u, p):
    s = ['N'] * (len(G)+1)  
    Q = []              
    Q.append(u)     
    s[u] = 'O'  
    while Q:
        u = Q.pop(0)  
        for v in G[u]:  
            if s[v] == 'N'
                s[v] = 'O'  
                p[v] = u  
                Q.append(v)  
        s[u] = 'C'
        print(Q)

def pathuv(u, v, p, path):
    while v != u and v != -1:
        path.append(v)
        v = p[v]
    path.append(v)

p = [-1] * (len(G)+1)
BFS(G, 1, p)
print(p)
print(pathuv(1, 9, p, path))