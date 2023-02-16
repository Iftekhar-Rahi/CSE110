canvas=int(input("Enter the amount of Canvas: "))
tube=int(input("Enter the amount of Tube: "))
total=(canvas*120)+(tube*75)
if canvas<0 :
    print("Canvas number can't be negative")
elif tube<0 :
    print("Tube number can't be negative")
elif total>=0 and total<=299:
    print(f"Previous total: {total}")
    print(f"New total after discount: {total}")
elif total>=300 and total<=499:
    print(f"Previous total: {total}")
    print(f"New total after discount: {total-10}")
elif total >= 500 and total <= 749:
    print(f"Previous total: {total}")
    print(f"New total after discount: {total - 20}")
elif total>=750 and total<=999:
    print(f"Previous total: {total}")
    print(f"New total after discount: {total-50}")
elif total>=1000:
    print(f"Previous total: {total}")
    print(f"New total after discount: {total-150}")