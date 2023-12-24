num=int(input())
sum=0
for i in range(1,num):
    if num%i==0:
        # print(i)
        sum+=i
# print(sum)
if num==sum:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")