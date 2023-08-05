#Ungraded 19
list_one = [1, 2, 2, 4, 5, 5, 7, 99, 200, 303, 70]
list_two = [1, 1, 2, 3, 3, 3, 4, 5, 200, 500, -5]
new=[]
for i in list_one:
     if i not in new:
         new.append(i)
for i in list_two:
    if i not in new:
        new.append(i)
print(new)