n = int(input())
a = []
b = []
AO = 0
BO = 0

a = input().split(" ")
b = input().split(" ")

for i in range(n):
	if(a[i][0]) == (b[i][0]):
		AO += 0
		BO += 0
	if(a[i][0]) == "r" and (b[i][0]) == "p":
		AO += 0
		BO += 1
	if(a[i][0]) == "r" and (b[i][0]) == "s":
		AO += 1
		BO += 0
	if(a[i][0]) == "p" and (b[i][0]) == "s":
		AO += 0
		BO += 1
	if(a[i][0]) == "p" and (b[i][0]) == "r":
		AO  += 1
		BO += 0
	if(a[i][0]) == "s" and (b[i][0]) == "r":
		AO += 0
		BO += 1
	if(a[i][0]) == "s" and (b[i][0]) == "p":
		AO += 1
		BO += 0

print(AO, BO)
