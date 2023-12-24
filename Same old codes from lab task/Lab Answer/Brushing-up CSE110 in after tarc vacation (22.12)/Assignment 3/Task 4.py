sum=0
for i in range(0,601,1):
    if i%9==0 and i%7==0:
        pass
    elif i%9==0 or i%7==0:
        sum+=i
print(sum)