#Ungraded 18
dict_1 = {'a' : 6, 'b' : 7, 'c' : 9, 'd' : 8, 'e' : 11, 'f' : 12, 'g' : 13}
low=int(input())
high=int(input())
new={}
for key,value in dict_1.items():
    if low<=value<high:
        new[key]=value
print(new)