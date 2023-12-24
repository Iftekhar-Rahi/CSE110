dict = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count=0
for i in dict.values():
    for c in i:
        count+=1
print(count)