loopVar = int(input())
c = []

for i in range(loopVar):
    c = []
    a,b = input("").split(" ",2)
    a = int(a)
    for i in range(a):
        c.append(b)
    print(*c,sep='')
