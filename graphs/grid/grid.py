from collections import deque
def main():
    inp = input().split(" ")
    n = int(inp[0])
    m = int(inp[1])
    matrix = []
    for i in range(n):
        l = []
        matrix.append(l)
        inp = input()
        for j in inp:
            l.append(int(j))

    p = BFS(matrix,n,m)
    print(backTrack(p,n,m))

def findNeighbour(i,j,val,n,m):
    l = []
    if j + val < m:
        l.append((i,j+val))
    if j - val >= 0:
        l.append((i,j-val))
    if i + val < n:
        l.append((i+val,j))
    if i - val >= 0:
        l.append((i-val,j))
    return l

def BFS(matrix,n,m):
    visited = set()
    l = findNeighbour(0,0,matrix[0][0],n,m)
    visited.add((0,0))
    queue = deque()
    queue.appendleft((0,0))
    res = []
    parents = {(0,0): None}

    while queue:
        v = queue.pop()
        res.append(v)
        x, y = v
        l = findNeighbour(x,y,matrix[x][y],n,m)
        for e in l:
            if e not in visited:
                queue.appendleft(e)
                visited.add(e)
                parents[e] = v
                if v == (n-1,m-1):
                    return parents
    return parents

def backTrack(parents, n, m):
    p = (n-1,m-1)
    count = 0
    while p:
        if p not in parents:
            return -1
        p = parents[p]
        count += 1
    return count -1

main()
