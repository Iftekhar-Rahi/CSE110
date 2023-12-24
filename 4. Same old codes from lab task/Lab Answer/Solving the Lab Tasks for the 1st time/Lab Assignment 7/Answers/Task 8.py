#Task 8
a=int(input())
def show_palindrome(limit):
  for count in range(1,limit+1):
    for i in range (2*(limit-count)):
      print("",end=" ")
    for i in range(1, count + 1):
      print(i, end=" ")
    for i in range(count - 1, 0, -1):
      print(i, end=" ")
    print()
show_palindrome(a)