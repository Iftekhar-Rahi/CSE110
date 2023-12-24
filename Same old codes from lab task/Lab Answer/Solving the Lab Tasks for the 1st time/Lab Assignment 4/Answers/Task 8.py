word=input("Enter  a number: ")
new=word[1: :2]
for ch in new:
    print(chr(ord(ch)-32),end="")