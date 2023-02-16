n=int(input())
counter=0
for i in range (1,n+1):
  if i==n:
    print(i)
    counter=counter+1
  elif n%i==0:
    print(i,end=", ")
    counter=counter+1
  else:
    pass
print(f"Total {counter} divisors.")