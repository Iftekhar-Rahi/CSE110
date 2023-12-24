n=input().split(",")
list_1=[]
new=[]
for i in n:
    list_1.append(int(i))
for c in list_1:
    if c not in new:
        new.append(c)
print(f"Input list: {list_1}")
print(f"Modified list: {new}")