n=int(input())
d={}
for i in range(n):
    key=input()
    value=input()
    d[key]=value
count=0
sum=0
for key,value in d.items():
    count+=1
    sum+=int(value)
avg=sum/count
print(f"Average is {avg}.")