s=int(input("Enter the distance in meter: "))
t=int(input("Enter the time in second: "))
v=(s/1000)/(t/3600)
print(f"{v} km/h")
if v<60:
    print("Too slow. Needs more changes.")
elif v>=60 and v<=90:
    print("Velocity is okay. The car is ready!")
elif v>90:
    print("Too fast. Only a few changes should suffice.")