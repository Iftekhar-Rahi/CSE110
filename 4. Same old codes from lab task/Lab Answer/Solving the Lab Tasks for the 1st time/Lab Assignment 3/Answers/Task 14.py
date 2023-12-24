sum=0
num=int(input())
for i in range(1,num):
  if num%i==0:
    sum=sum+i
if sum==num:
  print(f"{num} is perfect number")
else:
  print(f"{num} is not a perfect number")