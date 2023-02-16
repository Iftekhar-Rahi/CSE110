num=int(input("Enter the number: "))
if num>=0 and num<=100:
    if num>=90:
        print("A")
    elif num>=80 and num<90:
        print("B")
    elif num>=70 and num<80:
        print("C")
    elif num>=60 and num<70:
        print("D")
    elif num>=50 and num<60:
        print("E")
    elif num<50:
        print("F")
else:
    print("Invalid number")