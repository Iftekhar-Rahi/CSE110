num=int(input())
count=0
for i in range(1,num+1):
    if num%i==0:
        if i!=num:
            print(i,end=", ")
        else:
            print(i)
        count+=1
    else:
        pass
print(f"Total {count} divisors.")
