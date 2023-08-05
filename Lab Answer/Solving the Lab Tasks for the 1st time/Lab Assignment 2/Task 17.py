var1 = var2 = var3 = var4 = var5 = var6 = False
result1 = False
result2 = False
result3 = False
result4 = False
result5 = False
result6 = False
result7 = False
result8 = False
result9 = False
result10 = False
var1 = 4 > 3 - 1
var2 = var1 and False
var3 = True
var4 = False
var5 = True
var6 = var3 and False
result1 = (var1 or var2) and (8 * 10 > 45)
result2 = (var1 or var2) and (result1 and False)
result3 = (var1 and result1) or result2
result4 = (var1 or var2) or ((var3 and var1) and False)
result5 = (var1 and var2) and (result3 or var1)
result6 = ((var3 or var2) and not(result5)) or True
result7 = (var4 and result1) and ((result1 and False) or True)
result8 = ((var1 and result3) and (var5 or var6)) and True
result9 = ((result2 and var2) or (result7 and var1)) and False
result10 = not(var1 and True)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
