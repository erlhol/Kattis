from sys import stdin, stdout

class Node:
    def __init__(self,number):
        self.children = dict() # num = key, val = Node
        self.num = number
    
    def __str__(self) -> str:
        return " Number: "+str(self.num) +"Dict: "+ str(self.children)
    
def build_tree(number,root):
    p = root
    present_count = 0
    for i in range(len(number)):
        digit = number[i]
        if digit not in p.children.keys():
            p.children[digit] = Node(digit)
        else:
            present_count += 1
            p = p.children[digit]
            if not p.children:
                return False
            continue
        p = p.children[digit]
    
    return present_count != len(number)

def check_catalogue():
    n = int(stdin.readline())
    root = Node("-1")
    flag = True
    for x in range(n):
        number = stdin.readline().strip()
        if not build_tree(number,root):
            flag = False
    if flag:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")

def main():
    t = int(stdin.readline())
    for i in range(t):
        check_catalogue()
main()