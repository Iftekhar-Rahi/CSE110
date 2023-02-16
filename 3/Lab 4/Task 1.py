word=input()
new=""
for i in range(-1,-len(word)-1,-1):
    new+=word[i]
print(new)
print(word[-1:-(len(word)+1):-1])