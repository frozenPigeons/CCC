a = int(input())
d = []
e = []
comma = ","

for i in range(a):
    b,c = input().split(",",2)
    d.append(b)
    e.append(c)

d = sorted(d)
e = sorted(e)

highestX = 0
highestY = 0
lowestX = 0
lowestY = 0

highestX = int(d[0])
highestY = int(e[0])
lowestX = int(d[-1])
lowestY = int(e[-1])

highestX -= 1
highestY -= 1
lowestX += 1
lowestY += 1

print(str(highestX)+comma+str(highestY))
print(str(lowestX)+comma+str(lowestY))
