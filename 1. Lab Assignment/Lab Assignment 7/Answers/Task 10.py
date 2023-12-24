#Task 10
t=(1,4)
d={}
def make_square(num):
  for i in range(num[0],num[1]+1):
    d[i]=i*i
  return d
output=make_square(t)
print(output)