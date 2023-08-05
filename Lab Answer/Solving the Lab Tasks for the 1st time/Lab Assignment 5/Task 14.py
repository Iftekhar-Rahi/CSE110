myList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
b = []
index1 = 0
index2 = 0
index1 = 1
b = myList
while(index1<10):
    myList[index1] = index1+2
    index2 = 1
    while(index2<index1):
        myList[index1] = b[index1]+myList[index2]-index1
        index2 = index2+1
    print(myList[index1])
    index1 = index1+1