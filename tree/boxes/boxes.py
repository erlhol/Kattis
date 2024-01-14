from sys import stdin, stdout
from collections import defaultdict, deque

def main():

    n = int(stdin.readline())
    boxes = stdin.readline().strip().split(" ")
    l = list(int (i) for i in boxes)

    tree = buildTree(l)

    q = int(stdin.readline())
    for i in range(q):
        inp = stdin.readline().strip().split(" ")
        l = list(int (i) for i in inp)
        inp = l[1:]
        traverseTree(inp,tree,n)

def buildTree(inp):
    children = defaultdict(set)
    x = 1
    for i in inp:
        if i != 0:
            children[i].add(x)
        x+= 1

    return children

def traverseTree(query,tree,n):
    count = 0
    visitedSet = set()
    for i in query:
        # do BFS search from every root
        if i not in visitedSet:
            iteren = tree[i]
            vis = BFS(i,tree)
            visitedSet.update(vis)

    stdout.write(str(len(visitedSet))+"\n")

def BFS(start, children):
    visited = set()
    queue = deque()
    queue.appendleft(start)
    visited.add(start)
    while queue:
        v = queue.pop()
        edges = children[v]
        for u in edges:
            if u not in visited:
                queue.appendleft(u)
                visited.add(u)

    return visited


main()
