d=int(input())/1000
t=int(input())/3600
v=d/t
print(f"{v} km/h")
if v<60:
    print("Too slow. Needs more changes.")
elif v>=60 and v<=90:
    print("Velocity is okay. The car is ready!")
elif v>90:
    print("Too fast. Only a few changes should suffice.")