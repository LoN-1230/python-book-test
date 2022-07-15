n = int(input("請輸入大於 1 的整數:"))  
if (n > 1):
    for i in range(2, n):
        if(n%i == 0):
            print("%d 不是質數" % n)
            break
    else:
        print("%d 是質數" % n)
else:
    print("請輸入大於 1 的整數")

#上面是我寫的
#下面是教科書

n = int(input("請輸入大於 1 的整數:"))
if(n==2):
    print("2 是質數")
else:
    for i in range(2, n):
        if(n%i == 0):
            print("%d 不是質數" % n)
            break
    else:
        print("%d 是質數" % n)

del n
del i

            
        