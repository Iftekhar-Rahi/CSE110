word=input()
temp=None
for i in word:
    if i in ("1","0"):
        temp=True
    else:
        temp=False
if temp==True:
    print("Binary Number")
else:
    print("Not a Binary Number")