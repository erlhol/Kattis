from sys import stdin, stdout

def main():
    n = int(stdin.readline())

    inp = stdin.readline().split(" ")
    l = list(int(i) for i in inp)

    # pair the socks
    stack = l
    n_stack = []

    count = 0
    while stack:
        if n_stack and stack[-1] == n_stack[-1]:
            stack.pop()
            n_stack.pop()
        else:
            v = stack.pop()
            n_stack.append(v)
        count += 1

    if len(n_stack) > 0:
        stdout.write(str("impossible"))
    else:
        stdout.write(str(count))

main()
