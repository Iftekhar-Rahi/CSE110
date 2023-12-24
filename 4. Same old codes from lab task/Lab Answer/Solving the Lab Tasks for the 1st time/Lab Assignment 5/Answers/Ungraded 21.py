#Ungraded 21
word="0, 0, 1, 2, 3, 4,     4, 5, 6, 6, 6,      7, 8, 9, 4,     4"
space_removed_word=""
final_list=[]
all_numbers_int=[]
for i in word:
    if i!=" ":
        space_removed_word+=i
all_numbers_string=space_removed_word.split(",")
for i in all_numbers_string:
    all_numbers_int.append(int(i))
for i in all_numbers_int:
    if i not in final_list:
        final_list.append(i)
print(f"Given numbers in list: {all_numbers_int}")
print(f"List without any dupliacte values: {final_list}")