from math import ceil
problems = int(input())

for i in range(problems):
    how, out = input("").split(" ", 2) 
    how = int(how)
    out = int(out)
    div = ceil(how/out*100)
    if how > out:
        print("sus")
    elif div == 100:
        print("average")
    elif div >= 98 and div <= 99:
        print("below average")
    elif div >= 95 and div <= 97:
        print("can't eat dinner")
    elif div >= 90 and div <= 94:
        print("don't come home")
    elif div < 90:
        print("find a new home")
