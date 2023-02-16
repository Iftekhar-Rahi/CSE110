word=input().split(",")
a=[]
for i in word:
    a.append(int(i))
max=a[0]
for i in a:
    if i>max:
        max=i
print(f"My list: {a}")
print(f"Largest number in the list is {max} which was found at index {a.index(max)}.")