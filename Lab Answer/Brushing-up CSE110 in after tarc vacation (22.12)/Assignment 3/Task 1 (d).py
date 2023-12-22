count=1
for i in range(18,64,9):
    count+=1
    if count%2==0:
        print(i, end=", ")
    else:
        if i == 63:
            print(-i)
        else:
            print(-i, end=", ")