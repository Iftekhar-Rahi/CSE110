#Ungraded 16
word=input().split(", ")
new=[]
for i in word:
    new.append(int(i))
max=new[0]
for i in new:
    if i>max:
        max=i
second_max=new[0]
for i in new:
    if i<max:
        if i>second_max:
            second_max=i
print(f"My list: {new}")
print(f"Second largest number in the list is {second_max} which was found at index {new.index(second_max)}.")
