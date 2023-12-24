word=input("Enter a word: ")
if len(word)<4:
    if word[-2::] == "er":
        print(word[:-2:] + "est")
    else:
        print(word)
elif word[-3: : ]=="est":
    print(word)
elif word[-2: : ]=="er":
    print(word[ :-2: ]+"est")
elif len(word)>3:
    print(word+"er")