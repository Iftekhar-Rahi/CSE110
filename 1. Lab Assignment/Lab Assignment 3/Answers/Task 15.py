num=int(input())
counter=0
for i in range (1,num+1):
  if num%i==0:
    counter=counter+1
  else:
    pass
if counter==2:
  print(f"{num} is a prime number")
else:
  print(f"{num} is not a prime number")