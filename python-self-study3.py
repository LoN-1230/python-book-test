#2022/7/13
list1 = [1, 2, 3, 4, 5]
list2 = ["banana", "apple", "coco"]
list3 = [1, "banana", 3]
print(list1[3])
print(list3[2])
print(list2[-2])
#
list5 = [["joy", "1234"], ["mary", "abc"], ["ray", "5678"]]
print(list5[1])
print(list5[1][0])
#
score = [99, 100, 98]
print("國文成績: %d 分" % score[2])
print("數學成績: %d 分" % score[1])
print("英文成績: %d 分" % score[0])
#
r1 = range(5)
print(r1)
print(list(r1))
r2 = range(3, 8)
print(list(r2))
r3 = range(3, 8, 1)
r4 = range(3, 8, 2)
print(list(r4))
r5 = range(8, 3, -2)
print(list(r5))
#
list8 = ["香蕉", "蘋果", "橘子"]
for s in list8:
    print(s, end=",")
for i in range(1, 31):
    print(i, end="-")



