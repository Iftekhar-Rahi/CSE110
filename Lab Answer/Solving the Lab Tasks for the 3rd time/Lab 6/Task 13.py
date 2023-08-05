list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
d={}
for i in list_1:
    k,v=i
    if k in d.keys():
        d[k].append(v)
    else:
        d[k]=[v]
print(d)