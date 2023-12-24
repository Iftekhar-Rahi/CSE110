word=input()
new=""
for i in word:
    if i=="z" :
        new+="a"
    else:
        new+=chr(ord(i)+1)
print(new)