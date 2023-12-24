word=input("Enter a string: ")
checker=True
for i in word:
  if i=="1" or i=="0":
    pass
  else:
    checker=False
    break
if checker==True:
  print("Binary Number")
else:
  print("Not a Binary Number")