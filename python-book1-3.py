#2022/7/13
sum = 0
n = int(input("請輸入正整數:"))
for i in range(1, n+1):
    sum += i
print("1到%d的整數和為%d:" % (n, sum))
del n
del i
del sum
#
n = 0
for i in range(1,10001):
    for j in range(1,10001):
        n += 1
print(n)

