#Ungraded 20
word='The secret of getting ahead is getting started.'
special=['-', '=', '+', '*', '%']
word_w=word.split(" ")
sum=0
new={}
final={}
z=[]
for i in word_w:
    if i[-1]==".":
        i=i[0:-1]
    for c in i:
        sum+=ord(c)
    index=sum%len(special)
    if special[index] not in new.keys():
        new[special[index]] = [i]
    elif special[index] in new.keys():
        new[special[index]]+=[i]
    sum=0
#
for key,value in new.items():
    for c in value:
        if c not in z:
            z.append(c)
    final[key]=z
    z=[]

print(f"Answer : {final}")
