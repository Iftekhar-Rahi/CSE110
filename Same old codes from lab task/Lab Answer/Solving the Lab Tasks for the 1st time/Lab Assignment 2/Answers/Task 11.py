import math
s=int(input("Enter the value of S: "))
if s<100:
  # l=3000-125*math.pow(s,2)
  l=3000-125*s*s
else:
  l=12000/(4+(math.pow(s,2)/14900))
print(l)