cg=float(input("Enter your CGPA: "))
credit=int(input("Enter your total credit number: "))
if credit>=30:
  if cg>=3.8 and cg<=3.89:
    print("25 percent")
  elif cg>=3.9 and cg<=3.94:
    print("50 percent")
  elif cg>=3.95 and cg<=3.99:
    print("75 percent")
  elif cg==4:
    print("100 percent")
  elif cg>4:
    print("CGPA can't be more than 4")
  else :
    print("The student is not eligible for a waiver")

else :
  print("The student is not eligible for a waiver")