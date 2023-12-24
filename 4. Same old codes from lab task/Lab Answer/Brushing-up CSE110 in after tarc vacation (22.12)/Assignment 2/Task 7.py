num=int(input())
if num%2==0 and num%5==0:
    print("Multiple of 2 and 5 both")
elif num%2==0:
    print(num)
elif num%5==0:
    print(num)
else:
    print("Not a multiple we want")