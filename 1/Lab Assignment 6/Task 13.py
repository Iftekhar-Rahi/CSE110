list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
new={}
for i in list_1:
  key,value=i
  if key in new.keys():
    new[key].append(value)
  else:
    new[key]=[value]
print(new)