exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
n=int(input())
d={}
for key,value in exam_marks.items():
    if value>=n:
        d[key]=value
print(d)