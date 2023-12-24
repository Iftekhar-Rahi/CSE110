my_list=["hey", "there", "", "what's", "", "up", "", "?"]
a=[]
for i in my_list:
    if i=="":
        pass
    else:
        a.append(i)
print(a)