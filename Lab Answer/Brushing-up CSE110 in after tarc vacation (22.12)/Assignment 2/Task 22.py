canvas=int(input())
tube=int(input())
total=canvas*120 +tube*75
if 0<total<299:
    ans=total
elif 300<total<499:
    ans=total-10
elif 500<total<749:
    ans=total-20
elif 750<total<999:
    ans=total-50
elif total>=1000:
    ans=total-150
print(f"Previous total: {total}")
print(f"New total after discount: {ans}")