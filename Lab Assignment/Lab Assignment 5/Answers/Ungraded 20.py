#Ungraded 20
word="     [1,     2 ,     3, 50, 4]       "
new=[]
striped=word.strip()
if striped[0]=="[" and striped[-1]=="]":
    sq_removed=striped[1:-1]
print(f"Original data: {word}")
print(f"After removing square brackets: {sq_removed}")
noob_list=sq_removed.split(",")
print(f"Numbers in string format with extra white spaces: {noob_list}")
temp=""
for i in noob_list:
    for c in i:
        if c==" ":
            pass
        else:
            temp+=c
    new.append(int(temp))
    temp=""
print(f"Final data (numbers in list format): {new}")

