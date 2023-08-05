dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
counter=0
for key,value in dict_1.items():
  for i in value:
    counter+=1
print(counter)