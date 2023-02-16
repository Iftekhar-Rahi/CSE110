list1=[1, 4, 3, 2, 5]
list2=[8, 7, 6, 9]
flag=True
for i in list1:
    if i in list2:
        flag=True
    else:
        flag=False
print(flag)