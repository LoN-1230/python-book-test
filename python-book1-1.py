#2022/7/12 2-13
school = input("請輸入就讀學校")
name = input("請輸入名字")
nat = input("請輸入國文成績:")
math = input("請輸入數學成績:")
eng = input("請輸入英文成績:")
#print(type(nat))
sum = int(nat) + int(math) + int(eng)
#print(sum)
#print(type(sum))
average = sum / 3
#print(average)
print("就讀%4s %3s 成績總分: %3d 平均: %5.2f" %(school, name, sum, average))
del school
del name
del nat
del math 
del eng
del sum 
del average

