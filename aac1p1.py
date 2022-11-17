s, c = (input("").split(" ", 2))
s = int(s)
c = int(c)
if s**2 > c**2 * 3.14:
  print("SQUARE")
if c**2 * 3.14 > s**2:
  print("CIRCLE")
if c**2 * 3.14 == s**2:
  print("CIRCLE")
