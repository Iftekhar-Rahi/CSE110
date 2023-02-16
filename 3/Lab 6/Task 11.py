word="Python programming is fun"
word=word.lower()
d={}
for i in word:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print(d)