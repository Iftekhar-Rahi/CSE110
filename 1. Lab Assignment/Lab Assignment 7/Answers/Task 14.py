#Task 14
def rahi(sen,pos):
  a=""
  b=""
  for i in range (len(sen)): #rejected
    if i%pos==0 and i>=pos:
      a+=sen[i]
    elif i<=pos or i%pos !=0: #accepted
      b+=sen[i]
  return b+a
#===========
s=input()
p=int(input())
print(rahi(s,p))