#Task 12
def rahi(num):
  a=[]
  count=0
  for i in num:
    if a.count(i)<2:
      a.append(i)
    else:
      count+=1
  print(count)
  return a
print(rahi([1, 2, 3, 3, 3, 3, 4, 5, 8, 8]))