word=input("Enter a string: ")
for i in word:
    if i=="z":
        print(chr(ord("a")), end="")
    else:
        print(chr(ord(i)+1), end="")