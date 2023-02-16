sec=int(input("Enter the second: "))
hour=sec//3600
h_reminder=sec%3600
min=h_reminder//60
sec=h_reminder%60
print(f"{hour} hour {min} minute {sec} second")

