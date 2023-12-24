work_hour=int(input())
if work_hour>=0 and work_hour<=168:
    if work_hour<=40:
        salary=work_hour*200
        print(salary)
    elif work_hour>40:
        salary=8000+300*(work_hour-40)
        print(salary)
else:
    print("wrong time")