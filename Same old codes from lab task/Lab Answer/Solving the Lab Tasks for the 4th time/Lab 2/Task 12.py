time=int(input())
if time<0 or time>23:
    print("Wrong time")
elif 4<=time<=6:
    print("Breakfast")
elif time>=12 and time<=13:
    print("Lunch")
elif time>=16 and time<=17:
    print("Snacks")
elif 19<=time<=20:
    print("Dinner")
else:
    print("Patience is a virtue")