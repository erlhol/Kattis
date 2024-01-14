def main():
    n = input().split()
    capacity = int(n[0])
    stations = int(n[1])
    current = 0
    for i in range(stations):
        inp = input().split()
        left = int(inp[0])
        entered = int(inp[1])
        wait = int(inp[2])
        current += entered-left
        if ((i == 0) and left > 0):
            print("impossible")
            return
        if((current != capacity and wait > 0) or (current < 0 or current > capacity) ):
            print("impossible")
            return
        if (i == stations-1) and wait > 0:
            print("impossible")
            return
    if(current == 0):
        print("possible")
    else:
        print("impossible")
    

main()