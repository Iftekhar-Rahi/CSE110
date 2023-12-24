#Ungraded 17
word=input().split(", ")
new=[]
for i in word:
    new.append(int(i))
min=new[0]
for i in new:
    if i<min:
        min=i
max=new[0]
for i in new:
    if i>max:
        max=i
print(f"Smallest number in the list is {min} which was found at index {new.index(min)}")
print(f"Largest number in the list is {max} which was found at index {new.index(max)}")