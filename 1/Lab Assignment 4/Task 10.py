word=input("Enter a string: ")
counter=0
first=""
output=""
for ch in word:
  counter=counter+1
  if ch == ",":
    break
  first=first+ch
second=word[counter+1: :]
if len(first)==len(second):
  for i in range(len(first)):
    print(first[i]+second[i],end="")
elif len(first)>len(second):
  for i in range (len(first)):
    if i < len(second):
      output = output + first[i] + second[i]
    else:
      output = output + first[i]
  print(output)
elif len(first) < len(second):
  for i in range (len(second)):
    if i<len(first):
      output=output+first[i]+second[i]
    else:
      output=output+second[i]
  print(output)
