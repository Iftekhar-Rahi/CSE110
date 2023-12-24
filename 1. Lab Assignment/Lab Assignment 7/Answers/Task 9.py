#Task 9

def area_circumference_generator(r):
  import math
  area=r*r*math.pi
  circumference=2*r*math.pi
  tupple=area,circumference
  n1,n2=area,circumference
  print(tupple)
  print(f"Area of the circle is {n1} and circumference is {n2}")
area_circumference_generator(1)