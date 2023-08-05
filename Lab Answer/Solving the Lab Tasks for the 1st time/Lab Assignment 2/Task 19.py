var1 = var2 = var3 = var4 = var5 = var6 = False
result1 = result2 = result3 = result4 = result5 = result6 = False
result7 = result8 = result9 = result10 = False
var1 = (not False or False) and True
var2 = var1 and True
var3 = False and not True
var4 = True
var5 = False
var6 = var3 and True
result1 = (var1 and var2) and ( 40 % 3 > 45) or (var5 and var6)
result2 = (var1 or var2) or (result1 and False)
result3 = (var1 and result1) or result2 or var5
result4 = (var1 or var2) or ((var3 and var1) and False)
result5 = (var1 and var2) and (result3 or var1)
result6 = ((var3 or not var2) and (result5)) or True
result7 = (var4 and result1) and ((result1 and False) or True)
result8 = ((var1 and result3) and (not var5 or var6)) and True
result9 = ((result2 and var2) or (not result7 and var1)) and not False
result10 = not (var1 and True)
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
