#2022/7/13
pw = input("請輸入密碼")
if pw =="1234":
    print("密碼正確")
elif (int(pw) < 1000) or (int(pw) >= 10000):
    print("密碼是四位數")
#elif pw > ("%4s" % (pw)):
#    print("密碼是四位數")
#為什麼是用 pw > 4 才會執行print 不適應該用 < 嗎
#elif pw <= ("%5s" % (pw)):
#   print("密碼是四位數")
else: 
    print("密碼錯誤")
#分
score = input("請輸入成績")
if (int(score) > 100):
    print("成績輸入錯誤")
elif (int(score) >= 90):
    print("優等")
elif (int(score) >= 80):
    print("甲等")
elif (int(score) >= 70):
    print("乙等")
elif (int(score) >= 60):
    print("丙等")
else:
    print("丁等")

    
    


    
