from sys import stdin, stdout
from heapq import heappop, heappush

def main():
    inp = stdin.readline().strip().split(" ")
    n = int(inp[0])
    m = int(inp[1])
    k = int(inp[2])
    Q = [("Jane Eyre",k)]
    for i in range(n):
        inp = stdin.readline().strip().split("\"")
        heappush(Q,(inp[1],int(inp[2])))

    # read the books in order
    Q2 = []
    for i in range(m):
        inp = stdin.readline().strip().split("\"")
        mini = int(inp[0])
        name = str(inp[1])
        pages = int(inp[2])
        heappush(Q2,(mini,name,pages))


    minutesRead = 0
    while Q:
        name,min = heappop(Q)
        minutesRead += min
        if name == "Jane Eyre":
            stdout.write(str(minutesRead))
            return
        if Q2:
            index = Q2[0]
            min_n, name, pages = index
            while Q2:
                index = Q2[0]
                min_n, name, pages = index
                if min_n <= minutesRead:
                    index0 = heappop(Q2)
                    min_n,name,pages = index0
                    heappush(Q,(name,pages))
                else:
                    break

main()
