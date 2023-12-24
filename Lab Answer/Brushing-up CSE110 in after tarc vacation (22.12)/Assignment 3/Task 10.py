num=int(input())
while num!=0:
    ans=num%10
    if ans!=0:
        print(num % 10, end=", ")
    else:
        print(num % 10)
    num=num//10