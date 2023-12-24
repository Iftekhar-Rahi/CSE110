num=int(input())
count=1
while num>0:
    if num//10!=0:
        count+=1
    num=num//10
print(count)