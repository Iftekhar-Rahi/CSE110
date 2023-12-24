word=input().split(" ")
a=[]
b=[]
for i in word:
    i=int(i)
    if i%2!=0:
        a.append(i)
for i in word:
    b.append(int(i))
print(b)
print(a)