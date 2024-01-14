from sys import stdin, stdout
from collections import deque
from heapq import heappop, heappush

def main():
    for line in stdin:
        if line == '\n':
            break
        n = int(line)
        # each test is here
        queue = deque()
        stack = []
        pq = []
        resVerifyer = []
        queueRes = []
        stackRes = []
        pqRes = []
        structures = [queueRes,stackRes,pqRes]
        for i in range(n):
            inp = stdin.readline().strip().split(" ")
            a = int(inp[0])
            b = int(inp[1])
            if a == 1:
                queue.append(b)
                stack.append(b)
                heappush(pq,-b)
            else:
                resVerifyer.append(b)
                if queue or stack or pq:
                    queueRes.append(queue.popleft())
                    stackRes.append(stack.pop())
                    pqRes.append(-heappop(pq))

        count = 0
        for struct in structures:
            if struct == resVerifyer:
                count += 1

        if count > 1:
            print("not sure")
        elif pqRes == resVerifyer:
            print("priority queue")
        elif queueRes == resVerifyer:
            print("queue")
        elif stackRes == resVerifyer:
            print("stack")
        else:
            print("impossible")

main()
