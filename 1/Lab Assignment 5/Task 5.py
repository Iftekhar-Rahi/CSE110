list_1=["hey", "there", "", "what's", "", "up", "", "?"]
list_2=[]
for i in list_1:
    if i=="":
        pass
    else:
        list_2.append(i)
print(f"Original List: {list_1}")
print(f"Modified List: {list_2}")
