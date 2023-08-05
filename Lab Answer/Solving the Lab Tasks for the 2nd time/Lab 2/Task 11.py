import math

s=int(input("Enter the value of s: "))
if s<10:
    l=3000-125*math.pow(s,2)
elif s>=100:
    l=12000/(4+(math.pow(s,2)/14900))
print(l)