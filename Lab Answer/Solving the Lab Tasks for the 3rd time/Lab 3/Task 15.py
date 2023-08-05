num=int(input("Enter a number; "))
count=0
for i in range(2,int(num/2)):
    if num%i==0:
        count+=1
if count==0:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number.")
