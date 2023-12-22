hour=int(input())
if 0>hour or hour>168:
    print("Invalid hour")
elif hour<=40:
    print(hour*200)
elif hour>40:
    ans=8000+(hour-40)*300
    print(ans)
