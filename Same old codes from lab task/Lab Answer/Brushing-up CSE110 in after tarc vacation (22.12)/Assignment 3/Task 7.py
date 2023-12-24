count=0
sum=0
for _ in range(10):
    n=int(input())
    if n%2!=0:
        count+=1
        sum+=n
average=sum/count
print(sum)
print(average)