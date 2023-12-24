# Write a Python program that asks the user for a range (a starting number and an ending number)
# and then counts how many numbers are prime numbers and how many numbers are perfect
# numbers between that range. It also prints those numbers in the format shown in the output of
# the example given below.
#
s=int(input("Enter the starting value: "))
n=int(input("Enter the ending value: "))
counter=0
for i in range (s,n+1):
    for a in range(i+1):
        if i%a==0:
            counter+=1
            print(i,end=(","))