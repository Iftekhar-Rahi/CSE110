word=input().split(",")
a=[]
for i in word:
    a.append(int(i))
b=[]
b.append(a[0])
for i in a:
    if i not in b:
        b.append(i)
print(b)