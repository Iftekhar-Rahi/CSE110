n=int(input())
new={}
exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
for key,value in exam_marks.items():
  if value>n:
    new[key]=value
print(new)