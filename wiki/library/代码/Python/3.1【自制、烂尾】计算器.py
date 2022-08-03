print("请选择模式！")
print("1：加法计算")
print("2：减法计算")
print("3：乘法计算")
print("4：除法计算")
mode=input("选择模式：")
if mode=="1":
    print("已进入加法运算模式！")
    num1=input("输入加数1：")
    num2=input("输入加数2：")
    ans=num1+num2
    print(ans)
elif mode=="2":
    print("已进入减法运算模式！")
    num1=input("输入被减数：")
    num2=input("输入减数：")
    ans=num1-num2
    print(ans)
elif mode=="3":
    print("已进入乘法运算模式！")
    num1=input("输入乘数1：")
    num2=input("输入乘数2：")
    ans=num1*num2
    print(ans)
elif mode=="4":
    print("已进入除法运算模式！")
    num1=input("输入被除数：")
    num2=input("输入除数：")
    ans=num1/num2
    print(ans)
else:
    print("请选择正确的模式！")