#Task 3
n=int(input())
def foo_moo(num):
  if num%2==0 and num%3==0:
    print("FooMoo")
  elif num%2==0:
    print("Foo")
  elif num%3==0:
    print("Moo")
  else:
    print("Boo")
foo_moo(n)