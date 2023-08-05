#Task 5
a=int(input())
s=int(input())
d=input()
def calculate_tax(age,salary,designation):
  if designation== 'president':
    tax=0
    print(tax)
  elif salary>20000:
    tax=salary*0.1
    print(tax)
  elif 10000<=salary<=20000:
    tax=salary*0.05
    print(tax)
  elif  salary<10000:
    tax=0
    print(tax)
  elif age<18:
    tax=0
    print(tax)
calculate_tax(age=a,salary=s,designation=d)