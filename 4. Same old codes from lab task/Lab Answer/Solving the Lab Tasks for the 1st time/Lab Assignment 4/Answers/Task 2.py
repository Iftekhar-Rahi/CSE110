
word=input("Enter the string: ")
index=int(input("Enter the index where to reverse: "))
rest=word[index+1: : ]
reverse=word[index: :-1]
print(reverse+rest)