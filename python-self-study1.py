#2022/7/11
name = "danelee"
score = 99
print("%s 的成績為 %d" % (name, score))
#分
print("{} 的成績為 {}".format(name, score))
del name 
del score
#分
print(type(56))
print(type("how are you?"))
print(type(True))
#int 整數 flot浮點數 str 字串 bool 布林值
print("姓名   座號  國文  數學  英文")
print("%3s  %2d  %3d  %3d %3d" % ("lll", 1, 98, 100, 75))
print("%3s  %2d  %3d  %3d %3d" % ("je", 4, 100, 100, 100))
print("%3s  %2d  %3d  %3d %3d" % ("x", 21, 90, 85, 97))
# %Xs or %Xd or %Xf 就是佔X個字元 少於就填滿 大於??
#2022/7/12
num1 = 6 + 7.2
print(num1)
print(type(num1))
num2 = 6 + 6
print(num2)
print(type(num2))
num3 = 6 + True
print(num3)
print(type(num3))
del num1 
del num2
del num3
#bool 運算 True = 1, False = 0
score = 90
print("小小的成績為" + str(score))
del score
#str() int() flot() 強制轉換性質
score = input("請輸入數學成績")
print(score)
del score
#分
i = 2
i += 3
print(i)
del i
