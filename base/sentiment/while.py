# while语句

age = 1
while age < 5:
    num = age % 2
    if num == 0:
        print(age, num, "num is 偶数 ")
    else:
        print(age, num, "num is 奇数 ")
    age += 1

