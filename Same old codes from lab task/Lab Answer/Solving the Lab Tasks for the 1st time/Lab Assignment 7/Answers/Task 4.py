#Task 4
word=input()
def rahi(wordd):
  count_u=0
  count_l=0
  for i in wordd:
    if ord("A")<=ord(i)<=ord("Z"):
      count_u+=1
    elif ord("a")<=ord(i)<=ord("z"):
      count_l+=1
  print(f"No. of Uppercase characters : {count_u}")
  print(f"No. of Lowercase characters : {count_l}")
rahi(word)