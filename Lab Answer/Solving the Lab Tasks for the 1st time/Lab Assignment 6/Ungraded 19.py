#Ungraded 19
l=[(20, 'Sad'), (31, 'Sad'), (88, 'NotSad'), (27, 'NotSad')]
new={}
for i in l:
    key,value=i
    if value not in new.keys():
        new[value]=[i]
    else:
        new[value]+=[i]
print(new)

