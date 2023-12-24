#Task 15
def rahi(items,location="Dhanmondi"):
  d={"Rice":105,"Potato":20,"Chicken":250,"Beef":510,"Oil":85}
  sum=0
  for i in items:
    sum+=d[i]
  if location=="Dhanmondi":
    sum+=30
  else:
    sum+=70
  return sum
print(rahi(["Rice", "Beef", "Rice"]))