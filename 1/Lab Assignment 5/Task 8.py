list_1= [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [10, 11, 12, -13, -14, -15, -16]
new=[]
for i in list_1:
    if i%2==0:
        new.append(i)
for c in list_2:
    if c%2==0:
        new.append(c)
print(new)