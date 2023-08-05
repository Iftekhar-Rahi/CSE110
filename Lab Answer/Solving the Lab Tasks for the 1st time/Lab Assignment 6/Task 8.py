# word={'Jon':100, 'Dan':200, 'Rob':300}
n=int(input("Enter the length: "))
word={}
for i in range(n):
  key=input("Enter the key: ")
  value = int(input("Enter the value: "))
  word[key]=value




sum=0
count=0
for i in word.values():
  sum+=i
  count+=1
ava=sum/count
print(f"Average is {int(ava)}")