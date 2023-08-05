num=input()
ind=int(input())
extra=num[ind+1:]
rev=num[ind: :-1]
new=rev+extra
print(new)