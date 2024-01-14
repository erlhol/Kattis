from sys import stdin, stdout
from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(E,w,s,to):
    D = defaultdict(lambda: float('inf'))
    C = defaultdict(lambda: 0)
    Q = [(0,s)]
    D[s] = 0
    C[s] = 1
    while Q:
        cost,v = heappop(Q)
        for u in E[v]:
            c = cost + w[(v,u)]
            if D[u] > c:
                heappush(Q,(c,u))
                D[u] = c
                C[u] = C[v]    
            elif D[u] == c:
                C[u] += C[v]

    return C[to]

def main():
    V = set()
    E = defaultdict(set)
    W = dict()

    v, e = stdin.readline().strip().split(" ")
    for x in range(int(e)):
        inp = stdin.readline().strip().split(" ")
        u, v, w = [int (x) for x in inp]
        E[u].add(v)
        W[(u,v)] = w
        V.add(v)
        V.add(u)

    inp = stdin.readline().strip().split(" ")
    s, t = [int (x) for x in inp]
    print(dijkstra(E,W,s,t))

main()