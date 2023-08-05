#Ungraded 15
t=[(11, 22), (33, 55), (55, 77), (11, 44)]
new=[]
for i in t:
    key,value=i
    new.append(key*value)
print(new)
