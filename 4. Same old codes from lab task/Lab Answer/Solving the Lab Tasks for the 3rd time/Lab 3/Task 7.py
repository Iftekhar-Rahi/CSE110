count=0
sum=0
for i in range (1,11):
    num=int(input())
    if num%2!=0:
        count+=1
        sum+=num
    else:
        pass
avg=sum/count
print(f"The total of the odd numbers is {sum} and their average is {avg}")