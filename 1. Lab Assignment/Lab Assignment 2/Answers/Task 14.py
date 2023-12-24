s=int(input("Enter the distance in meter: "))
t=int(input("Enter the time in second: "))
s=s/1000
t=t/3600
v=s/t
if v<60:
  print(f"{v} km/h")
  print("Too slow. Needs more changes.")
elif v>=60 and v<=90:
  print(f"{v} km/h")
  print("Velocity is okay. The car is ready!")
else:
  print(f"{v} km/h")
  print("Too fast. Only a few changes should suffice.")