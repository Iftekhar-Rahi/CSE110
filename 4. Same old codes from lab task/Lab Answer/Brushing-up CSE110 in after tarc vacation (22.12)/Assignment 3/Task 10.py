num=int(input())
while num!=0:
    ans=num%10
    num = num // 10
    if num!=0:
        print(ans, end=", ")
    else:
        print(ans % 10)
