from sys import stdin, stdout
from collections import defaultdict

def main():
    inp = stdin.readline().split(" ")
    l = defaultdict(int)
    n = int(inp[0])
    q = int(inp[1])
    for i in range(q):
        inp = stdin.readline().split(" ")
        ins = inp[0]
        if ins == 'SET':
            i2 = int(inp[1])
            x = int(inp[2])
            setting(i2,x,l)
        elif ins == 'PRINT':
            i2 = int(inp[1])
            printing(i2,l)
        elif ins == 'RESTART':
            y = int(inp[1])
            l = restart(y,l,n)

def setting(i,x,l):
    l[i] = x

def printing(i,l):
    stdout.write(str(l[i])+"\n")

def restart(x,l,n):
    l = defaultdict(lambda: x)
    return l

main()
