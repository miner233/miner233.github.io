import random
while True:
    num1=random.choice(range(100))
    num2=random.choice(range(100))
    jifeng=0
    num3=num1+num2
    print(num1,"+",num2,"= ?")
    ans=input("输入答案：")
    if ans==num1+num2:
        print("恭喜你，答对了！")
        jifeng=jifeng+1
        print("当前积分：",jifeng)
    else:
        print("你答错了。",num1,"+",num2,"的结果是",num3)
        print("当前积分：",jifeng)