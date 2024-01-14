import math
from heapq import heappush, heappop
from sys import stdin, stdout

def prim(V): # finner det minimale spenntreet til G
    s = V[0]
    Q = [(0,s)]
    visited = set()
    count = 0

    while Q and len(V) > len(visited):
        w,v = heappop(Q)
        if v in visited:
            continue
        visited.add(v)
        count += w

        for u in V:
            if u != v and u not in visited:
                weight = calculateDistance(v,u)
                heappush(Q,(weight,u))

    return count

def calculateDistance(x,y):
    x1, x2 = x
    y1, y2 = y
    return math.sqrt((x1-y1)**2+(x2-y2)**2)

n = int(stdin.readline())
output = []
for i in range(n):
    m = int(stdin.readline())

    V = []
    for i in range(m):
        x,y = stdin.readline().strip().split(" ")
        V.append((float(x),float(y)))

    p = prim(V)
    stdout.write(str(p)+"\n")
