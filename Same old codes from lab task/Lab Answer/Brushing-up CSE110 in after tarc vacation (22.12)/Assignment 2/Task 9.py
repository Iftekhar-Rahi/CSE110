num=int(input())
hour=num//3600
hour_reminder=num%3600
minute=hour_reminder//60
second=hour_reminder%60
print(f"Hours: {hour} Minute: {minute} Second: {second}")