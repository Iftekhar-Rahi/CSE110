a=input().split(", ")
new=a[2:-2]
new_1=[]
if len(a)<4:
    print("Not possible")
else:
    for i in new:
        new_1.append(int(i))
    print(new_1)
