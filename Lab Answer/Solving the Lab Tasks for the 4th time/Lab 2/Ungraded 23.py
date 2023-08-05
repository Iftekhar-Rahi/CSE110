#(degrees Celsius) = ((degrees Fahrenheit) - 32) * 0.56
f=float(input())
c=(f-32)*0.56
result=round(c,2)
if result-int(result)==0:
    print(f"{int(result)} degrees C")
else:
    print(f"{result} degrees C")
if result>=30:
    print("Summer")
elif 25<result<30:
    print("Spring")
elif 20<=result<=25:
    print("Autumn")
elif result<20:
    print("Winter")