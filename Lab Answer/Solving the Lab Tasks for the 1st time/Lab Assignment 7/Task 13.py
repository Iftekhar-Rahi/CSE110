#Task 13
o=input()
num1=int(input())
num2=int(input())
def rahi(o,num1,num2):
  if o=="+":
    s=num1+num2
  elif o=="-":
    s=num1-num2
  elif o=="*":
    s=num1*num2
  elif o=="/":
    s=num1/num2
  return s
print(rahi(o,num1,num2))