word_1="Python programming is fun"
word=word_1.lower()
new={}
for i in word:
  if i!=" ":
      if i in new.keys():
        new[i]+=1
      else:
        new[i]=1
print(new)