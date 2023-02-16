word="AAABBBBCDDBBECE"
new=word[0]
for i in word:
    if i==new[-1]:
        pass
    else:
        new += i
print(new)