# Python input 函数
input 函数：用户从键盘输入内容并返回
## 基本语法
```Python
input("提示语")
input(a)
input(a,"提示语")
```

## 温馨提示
input 函数返回的值为字符串，因此若要进行计算，请使用 int() 或 float() 将返回的值转换为数后计算。

## 代码示例
```Python
name1=input("请输入你的名字：")
name2=input("请输入你朋友的名字：")
age1=input("请输入你的年龄：")
age2=input("请输入你朋友的年龄：")
age1=int(age1)
age2=int(age2)
if age1 > age2:
    print("你的年龄大一些，大",age1-age2,"岁。")
elif age1 = age2:
    print("你们俩的年龄相等，是",age1,"岁。")
else:
    print("你朋友的年龄大一些，大",age2-age1,"岁。")
```