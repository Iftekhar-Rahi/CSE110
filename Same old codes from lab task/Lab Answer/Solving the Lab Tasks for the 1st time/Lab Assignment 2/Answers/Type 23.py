f=int(input("Enter the temperature in degrees Fahrenheit: "))
c=.56*(f-32)
c=round(c,2)
k=str(c)
if k[-2:]==".0" :
    c=int(c)
# c=int(c)
print(f"{c} degrees C")
if c<20:
    print("Winter")
elif c>=20 and c<=25:
    print("Autumn")
elif c>25 and c<30:
    print("Spring")
elif c>=30:
    print("Summer")
