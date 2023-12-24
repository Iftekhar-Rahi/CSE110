num=int(input())
new=num
while new>0:
    last = new % 10
    new = num // 10
    num=new
    if num==0:
        print(last)
    else:
        print(last, end=', ')