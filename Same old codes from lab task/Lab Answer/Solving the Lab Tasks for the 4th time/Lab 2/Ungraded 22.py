canv=int(input())
tube=int(input())
total=(canv*120)+(tube*75)
print(f"Previous total: {total}")
if total>=1000:
    print(f"New total after discount: {total-150}")
elif 750<=total<=999:
    print(f"New total after discount: {total - 50}")
elif 500<=total<=749:
    print(f"New total after discount: {total - 20}")
elif 300<=total<=499:
    print(f"New total after discount: {total - 10}")
elif 0<=total<=299:
    print(f"New total after discount: {total - 20}")
