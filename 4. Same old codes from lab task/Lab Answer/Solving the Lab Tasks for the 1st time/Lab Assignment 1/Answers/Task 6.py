weight=int(input("Enter the amount of Weight: "))
# floor_div= weight//4
# ans=floor_div*4
# print (f"You can carry maximum {ans}")
ans=weight-(weight%4)
print (f"You can carry maximum {ans}")