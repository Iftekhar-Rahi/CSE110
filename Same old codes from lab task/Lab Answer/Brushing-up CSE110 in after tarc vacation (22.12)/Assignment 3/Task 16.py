test=int(input())
sum=0
counter=1
number=int(input())
sum+=number
min=number
max=number
for i in range(test-1):
        new_number=int(input())
        if new_number>=max:
            max=new_number
        elif  new_number<=min:
            min=new_number
        sum+=new_number
        counter+=1
average=sum/counter
print(max)
print(min)
print(average)

