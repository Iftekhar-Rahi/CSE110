q=int(input())
sum=0
n=int(input())
sum+=n
max=n
min=n
for i in range(q-1):
    num=int(input())
    if num>max:
        max=num
    if num<min:
        min=num
    sum+=num
avg=sum/q
print(f"Maximum {max}")
print(f"Minimum {min}")
print(avg)
