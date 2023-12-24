#Ungraded 16
a_tuple = ( [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
new=[]
n=input()
for i in a_tuple:
    one=i[0:2]+[n]
    new.append(one)
print(new)