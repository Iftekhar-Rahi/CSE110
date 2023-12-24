# num=int(input())
# var=2
# for r in range(num):
#     if num+2==var:
#         break
#     for i in range(1,var):
#         print(i,end="")
#     print()
#     var+=1

num=int(input())
for r in range(1,num+1):
    for c in range(1,r+1):
        print(c,end="")
    print()