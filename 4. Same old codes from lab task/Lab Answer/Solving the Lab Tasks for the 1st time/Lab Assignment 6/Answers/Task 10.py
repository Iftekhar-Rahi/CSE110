#Task 10
d={'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
new_keys=[]
new_values=[]
for key,value in d.items():
  new_keys.append(key)
  new_values.append(value)
max=new_values[0]
for i in new_values:
  if i>max:
    max=i
print(f"The highest selling book genre is '{new_keys[new_values.index(max)]}' and the number of books sold are {max}.")