money =int(input("請輸入購物金額"))
if (money >= 10000):
    if (money >= 100000):
        print(str(money * 0.8), end=" 元\n")
    elif (money >= 50000):
        print(str(money * 0.85), end=" 元\n")
    elif (money >= 30000):
        print(str(money * 0.9), end=" 元\n")
    else:
        print(str(money * 0.95), end=" 元\n")
else:
    print(str(money), end=" 元\n")
#以上是書本的想法
del money
#以下是我的想法
money = input("請輸入購物金額")
if (int(money) >= 100000):
    print(int(money) * 0.8 + " 元")
elif (int(money) >= 50000):
    print(int(money) * 0.85 + " 元")
elif (int(money) >= 30000):
    print(int(money) * 0.9 + " 元")
elif (int(money) >= 10000):
    print(int(money) * 0.95 + " 元")
else:
    print(money + " 元")
#書本那樣是可以讓電腦跑簡單一點嗎?(而且看起來好像順一點




    
    
    

    