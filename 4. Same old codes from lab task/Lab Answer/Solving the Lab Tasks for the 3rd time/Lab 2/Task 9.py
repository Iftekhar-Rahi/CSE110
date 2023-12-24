num=int(input())
hour=num//3600
h_remain=num%3600
min=h_remain//60
sec=min_remain=h_remain%60
print(f"Hours: {hour} Minutes: {min} Seconds: {sec}")