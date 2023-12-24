time=int(input("Enter the time: "))
if time<0 or time>24:
  print("Wrong time")
elif time>=4 and time<=6 :
  print("Breakfast")
elif time>=12 and time <=13:
  print("Lunch")
elif time>=16 and time <=17:
  print("Snacks")
elif time>=19 and time <=20:
  print("Dinner")
else:
  print("Patience is a virtue")