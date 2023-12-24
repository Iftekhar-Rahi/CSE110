n=int(input("Enter a number: "))
# counter=0
while n!=0:
    c=n%10
    n=n//10
    if n!=0:
      print(c,end=", ")
    else:
      print(c)