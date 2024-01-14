from sys import stdin, stdout
from collections import defaultdict
from typing import Pattern
def main():
    n = int(stdin.readline())
    E = defaultdict(set) # bruke .update() for å legge inn alle
    for i in range(n):
        inp = stdin.readline().strip().split(" ")
        a = inp[0]
        edges = inp[1:]
        E[a].update(edges)
        for e in edges:
            E[e].add(a)
    
    destination = stdin.readline().strip().split(" ")
    fr = destination[0]
    to = destination[1]

    d = DFS(E,fr,to)
    backTrack(to,d)

def DFS(E, fr,to):
    v = fr
    visited = set()
    visited.add(v)
    stack = [v]
    parents = {v: None}
    while stack:
        v = stack.pop()
        for e in E[v]:
            if e not in visited:
                visited.add(e)
                stack.append(e)
                parents[e] = v
                if e == to:
                    return parents
    return parents

def backTrack(to, parents):
    p = to
    route = ""
    while p:
        route = p + " " +route
        if p not in parents:
            stdout.write("no route found")
            return
        p = parents[p]
        
    if route:
        stdout.write(route[:-1])
    else:
        stdout.write("no route found")
    

main()