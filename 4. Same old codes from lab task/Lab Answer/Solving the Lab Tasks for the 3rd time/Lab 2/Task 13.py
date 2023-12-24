num=int(input())
if num>=0 and num<=100:
    if num>=90:
        print("A")
    elif 80<=num<90:
        print("B")
    elif 70<=num<80:
        print("C")
    elif 60<=num<70:
        print("D")
    elif 50<=num<60:
        print("E")
    else:
        print("F")
else:
    print("Invalid number")