num=int(input())
sum=0
counter=0
for i in range (num):
  n=int(input())
  if counter==0:
    max=n
    min=n
  if n>=max:
    max=n
  if n<=min:
    min=n
  sum=sum+n
  counter=counter+1
average=sum/num
print(f"Maximum {max}")
print(f"Minimum {min}")
print(f"Average {average}")