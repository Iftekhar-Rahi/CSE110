word=input()
new=""
for i in range(len(word)):
    if word[i]==",":
        first=word[:i]
        sec=word[i+2:]
if len(first)>len(sec):
    for i in range (len(sec)):
        new+=first[i]+sec[i]
    new=new+first[len(sec)+1:]
    print(new)
else:
    for i in range(len(first)):
        new += first[i] + sec[i]
    new =new+sec[len(first)+1:]
    print(new)