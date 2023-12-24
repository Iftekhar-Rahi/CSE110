#Task 11
def rem_dublicate(t):
    l=[]
    for i in t:
        if i not in l:
            l.append(i)
        else:
            pass
    final=tuple(l)
    return final
f=rem_dublicate(("Hi", 1, 2, 3, 3, "Hi",'a', 'a', [1,2]))
print(f)