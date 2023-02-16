hour=int(input())
if hour>=0 and hour<=23:
    if 4<=hour<=6:
        print("Breakfast")
    elif 12<=hour<=13:
        print("Lunch")
    elif 16<= hour <= 17:
        print("Snacks")
    elif 19 <= hour <= 20:
        print("Dinner")
    else:
        print("Patience is a virtue")
else:
    print("Wrong time")