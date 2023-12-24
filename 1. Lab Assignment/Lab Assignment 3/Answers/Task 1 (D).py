counter=1
for i in range (18,64,9):
    if counter%2==0:
      if i!=63:
        print(i*-1 ,end=", ")
      elif i==63:
        print(i*-1)
    else:
      print(i, end=", ")
    counter=counter+1