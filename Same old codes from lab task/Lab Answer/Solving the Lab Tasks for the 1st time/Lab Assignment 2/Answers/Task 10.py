hour=int(input("Enter the hour: "))
if hour>=0 and hour<=168:
  if hour<=40:
    salary=hour*200
    print(salary)
  else:
    reminder=hour-40
    salary=8000+(reminder*300)
    print(salary)
elif hour<0:
  print("Hour cannot be negative")
else:
  print("Impossible to work more than 168 hours weekly")