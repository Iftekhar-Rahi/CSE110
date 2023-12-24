word=input()
new=""
new1=""
for i in range(1,len(word)+1,2):
    new+=word[i]
for i in new:
    if ord("A")<=ord(i)<=ord("Z"):
        new1+=i
    else:
        new1 += chr(ord(i) - 32)
print(new1)