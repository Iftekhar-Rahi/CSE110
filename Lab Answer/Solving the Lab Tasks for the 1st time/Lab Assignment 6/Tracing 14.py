dict1 = {'a':59 , 'b':-82 , 'c':5 , 'd':-81 , 'e':53}
for i in dict1:
    j = 0
    k = 22
    while j < 5:
        if j % 2 == 0:
            k = dict1[i] + j - (8 + k % 6) / 3
            dict1[i] = dict1[i]+ int(k)
        else:
            k = dict1[i] + j - (6 - k % 8) * 3
            dict1[i] = dict1[i] - int(k)
        j += 1
    print(int(k))
    print(i + " -> " + str(dict1[i]))```