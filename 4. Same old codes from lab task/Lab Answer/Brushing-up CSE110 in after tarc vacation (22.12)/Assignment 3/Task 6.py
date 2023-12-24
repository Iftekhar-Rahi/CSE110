n=int(input())
count=1
sum=0
for i in range(1,n+1,1):
    if count%2==0:
        sum-=i*i
    else:
        sum+=i*i
    count+=1
print(sum)