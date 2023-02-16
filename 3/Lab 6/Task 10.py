d={'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
new_keys=[]
new_value=[]
for key,value in d.items():
    new_keys.append(key)
    new_value.append((value))
large=new_value[0]
for i in new_value:
    if i>large:
        large=i
print(f"The highest selling book genre is '{new_keys[new_value.index(large)]}' and the number of books sold are {large}.")