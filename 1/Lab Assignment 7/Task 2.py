#Task 2
limit=int(input())
def fibonacci(num):
  n1=0
  print(n1,end=" ")
  n2=1
  print(n2,end=" ")
  for i in range (num):
    n3=n1+n2
    if n3>limit:
      break
    else:
      print(n3,end=" ")
      n1=n2
      n2=n3
fibonacci(limit)