n=int(input("Enter a number: "))
m=n
c=0
while m!=0:
  m=m//10
  c=c+1
pow=10**(c-1)

while n!=0:
  a=n//pow
  n=n%pow
  pow=pow//10
  if n==0:
    print(a)
  else:
    print(a, end=", ")