num=int(input())
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
if flag==True:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")