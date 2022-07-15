f = int(input("請輸入大樓的樓層數:"))
print("本大樓具有樓層數:")
if (f>3):
    f += 1
for i in range(1, f+1):
    if (i==4):
        continue
    print(i, end=" ")
#此程式是要跳過4樓的名字

del f
del i