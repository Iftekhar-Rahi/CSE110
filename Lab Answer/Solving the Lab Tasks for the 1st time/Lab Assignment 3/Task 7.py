sum = 0
counter = 0
for i in range(1, 11, 1):
    c = int(input())
    if c % 2 != 0:
        sum = sum + c
        counter = counter + 1
    else:
        pass

average = sum / counter
print(f"The total of the odd numbers is {sum} and their average is {average}")