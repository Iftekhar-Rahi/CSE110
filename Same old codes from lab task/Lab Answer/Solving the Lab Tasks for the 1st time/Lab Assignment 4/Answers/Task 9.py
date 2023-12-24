word=input("ENTER A STRING: ")
new=word[0]
for i in word:
  if i==new[-1]:
    pass
  else:
    new=new+i
print(new)