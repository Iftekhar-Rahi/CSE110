num=int(input())
a=num
count=0
while num!=0:
    num=num//10
    count+=1

while a!=0:
    b=a//10**(count-1)
    if count!=1:
        print(b,end=", ")
    else:
        print(b)
    a=a % (10 ** (count - 1))
    count-=1
