num=int(input())
if num<0 or num>100:
    print("Invalid number")
else:
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
    else:
        print("F")