word=input()

if word[-2::1]=="er":
    new=word[0:len(word)-1]+"st"
    print(new)
elif word[-3::1]=="est":
    print(word)
elif len(word)<4:
    print(word)
elif len(word)>3:
    new=word+"er"
    print(new)
