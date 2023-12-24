#Ungraded 18
word=input().split(", ")
word_2=input().split(", ")
new=[]
for i in word:
    if i in word_2:
        new.append(i)
print(new)