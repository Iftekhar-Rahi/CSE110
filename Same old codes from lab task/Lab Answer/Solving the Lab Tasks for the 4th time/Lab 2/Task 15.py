cg=float(input())
credit=int(input())
if credit>=30:
    if 3.8<=cg<=4:
        if cg==4:
            print("The student is eligible for a waiver of 100 percent")
        elif 3.95<=cg<=3.99:
            print("The student is eligible for a waiver of 75 percent")
        elif 3.90<=cg<=3.94:
            print("The student is eligible for a waiver of 50 percent")
        elif 3.80<=cg<=3.89:
            print("The student is eligible for a waiver of 25 percent")
    else:
        print("The student is not eligible for a waiver")
else:
    print("The student is not eligible for a waiver")