cgpa=float(input())
credit=int(input())
if credit>30:
    if cgpa>=3.8 and cgpa<3.89:
        print('25 percent')
    elif cgpa>=3.90 and cgpa<3.94:
        print("50 percent")
    elif cgpa>=3.95 and cgpa<3.99:
        print("75 percent")
    elif cgpa==4.00:
        print("100 percent")
    else:
        print('The student is not eligible for a waiver')
else:
    print('The student is not eligible for a waiver')