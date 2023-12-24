h=int(input())
if h<0 or h>168:
    if h<0:
        print("Hour cannot be negative")
    else:
        print('Impossible to work more than 168 hours weekly')
else:
    if h<=40:
        print(h*200)
    else:
        print(8000+((h-40)*300))