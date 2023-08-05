num=int(input("Enter the time: "))
if num>=0 and num<24:
    if num>=4 and num<=6:
        print("Breakfast")
    elif num>=12 and num<=13:
        print("Lunch")
    elif num>=16 and num <=17:
        print("Snacks")
    elif num >= 19 and num <= 20:
        print("Dinner")
    else:
        print("Patience is a virtue")
else:
    print("Wrong time")