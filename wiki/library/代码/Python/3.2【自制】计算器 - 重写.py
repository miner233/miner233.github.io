# 开始循环
while True:
    # 定义加法运算
    def jiafa(a,b):
        return a + b
    # 定义减法运算
    def jianfa(a,b):
        return a - b
    # 定义乘法运算
    def chengfa(a,b):
        return a * b
    # 定义除法运算
    def chufa(a,b):
        return a / b
    
    # 打印模式选择提示
    print("请选择你要使用的模式！输入数字即可")
    print("1：加法运算")
    print("2：减法运算")
    print("3：乘法运算")
    print("4：除法运算")
    print("5：退出")
    # 设置变量 mode 模式
    mode=input("选择你的模式：")
    # 检测选择的模式
    if mode=="1":
        # 加法运算模块
        num1=int(input("输入加数1："))
        num2=int(input("输入加数2："))
        print(num1,"+",num2,"=",jiafa(num1,num2))
    elif mode=="2":
        # 减法运算模块
        num1=int(input("输入被减数："))
        num2=int(input("输入减数："))
        print(num1,"-",num2,"=",jianfa(num1,num2))
    elif mode=="3":
        # 乘法运算模块
        num1=int(input("输入乘数1："))
        num2=int(input("输入乘数2："))
        print(num1,"×",num2,"=",chengfa(num1,num2))
    elif mode=="4":
        # 除法运算模块
        num1=int(input("输入被除数："))
        num2=int(input("输入除数："))
        print(num1,"÷",num2,"=",chufa(num1,num2))
    elif mode=="5":
        print("程序已退出")
        break
    else:
        print("请选择正确的模式！")