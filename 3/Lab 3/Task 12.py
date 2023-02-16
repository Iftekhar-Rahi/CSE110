import math
num=int(input())
def digit_counter(num):
    count = 1
    while num > 0:
        if num // 10 != 0:
            count += 1
        num = num // 10
    return count
counter=digit_counter(num)

while num>0:
    first = num // (math.pow(10, counter - 1))
    num = num % (math.pow(10, counter - 1))
    if num==0:
        print(int(first))
    else:
        print(int(first), end=", ")
    counter-=1