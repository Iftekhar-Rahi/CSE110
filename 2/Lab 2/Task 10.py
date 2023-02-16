num=170
if num>=0:
    if num <= 40:
        total = num * 200
        print(total)
    elif num>40 and num<=168:
        total=8000+300*(num-40)
        print(total)
    else:
        print("Impossible to work more than 168 hours weekly")

else:
    print("Hour cannot be negative")