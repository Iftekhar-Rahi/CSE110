num=int(input())
hour=num//3600
hour_remaining=num%3600
min=hour_remaining//60
sec=hour_remaining%60
print(f"Hours: {hour} Minutes: {min} Seconds: {sec}")