sec=int(input("Enter the second: "))
hour=sec//3600
sec_remain=sec%3600
minute=sec_remain//60
sec_ab=sec_remain%60
print(f"{hour} hour {minute} minute {sec_ab} second")