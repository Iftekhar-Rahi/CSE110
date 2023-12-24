s=int(input())
t=int(input())
v=(s/1000)/(t/3600)
print(f"{v} km/h")
if v<60:
    print("Too slow. Needs more changes.")
elif v>=60 and v<=90:
    print("Velocity is okay. The car is ready!")
elif v>=90:
    print("Too fast. Only a few changes should suffice.")