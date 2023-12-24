word=input()
flag=None
for i in range(len(word)):
    if word[i]=="1" or word[i]=="0":
        flag=True
    else:
        flag=False
        break
if flag==True:
    print("Binary Number")
else:
    print("Not a Binary Number")