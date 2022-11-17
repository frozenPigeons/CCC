trinum = input()
rag = 0
trinum = int(trinum)


for rag in range(trinum):
    s1, s2, s3 = input().split(" ", 3)

    s1 = int(s1)
    s2 = int(s2)
    s3 = int(s3)

    if s1 > s3:
      replace = s3
      s3 = s1
      s1 = replace
    if s2 > s3:
      replace = s3
      s3 = s2
      s2 = replace

    if s1*s1 + s2*s2 == s3*s3:
      print("R")
    elif s1*s1 + s2*s2 > s3*s3:
      print("A")
    elif s1*s1 + s2*s2 < s3*s3:
      print("O")
