l= list(range(1001))
guess = 10
low = 0
high = len(l)
while guess > 0:
    i = (low+high)//2
    print(i,flush = True)
    inp = input()
    if inp == "lower":
        high = i
    elif inp == "higher":
        low = i
    else:
        break
    guess -= 1