print("a in while loop")
i=24
while i>=-6:
    if i==-6:
        print(i)
    else:
        print(i,end=", ")
    i=i-6
print("a in for loop")
for i in range (24,-7,-6):
    if i==-6:
        print(i)
    else:
        print(i,end=", ")
print("b")
for i in range (-10,21,5):
    if i==20:
        print(i)
    else:
        print(i,end=", ")
print("C")
for i in range (18,64,9):
    if i==63:
        print(i)
    else:
        print(i,end=", ")
print('D')
count=1
for i in range (18,64,9):
    if count%2==0:
        if i == 63:
            print(-i)
        else:
            print(-i, end=", ")
    else:
        if i == 63:
            print(i)
        else:
            print(i, end=", ")
    count+=1
