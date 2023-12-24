#Task 7
a=int(input())
def show_palindrome(limit):
  for i in range(1,limit+1):
    print(i,end="")
  for i in range(limit-1,0,-1):
    print(i,end="")
show_palindrome(a)

