import math
radius=float(input("Please enter the radius value: "))
# a=math.pi*radius*radius
a=math.pi*math.pow(radius,2)
c=2*math.pi*radius
print(f"Area is {a}")
print(f"Circumference is {c}")