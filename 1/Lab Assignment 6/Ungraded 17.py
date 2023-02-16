#Ungraded 17
my_dictionary = {'c1':'Red', 'c2':'Green', 'c3':None, 'd4':'Blue', 'a5':None}
new={}
for key,value in my_dictionary.items():
    if value==None:
        pass
    else:
        new[key]=value
print(new)