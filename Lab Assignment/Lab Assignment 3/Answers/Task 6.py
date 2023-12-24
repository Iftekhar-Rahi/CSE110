sum=0
num=int(input())
for i in range (1,num+1,1):
    if i%2==0:
      sum=sum-i**2
    else:
      sum=sum+i**2
print(sum)