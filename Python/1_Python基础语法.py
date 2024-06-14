#Python基础语法

#1. python保留字
##读取标准库中全部的保留字
import keyword
keyword.kwlist
##注：使用交互模式，用脚本模式跑不出来


#2. 注释
##实例一：单行注释
print("单行注释已学会！")#第二个注释

##实例二：多行注释
'''
第三注释
第四注释

'''

"""
第五注释
第六注释
"""
print("多行注释已学会！")


#3. 缩进
##实例一：
if True: #这个冒号应该很容易丢掉
    print("True")
else: #缩进与if对齐
    print("False")#与上一个print命令对齐
#4. 多行语句
##用反斜杠\进行多行语句编写
item_one,item_two,item_three=1,2,3
total=item_one+\
      item_two+\
      item_three
print(total)
##用括号进行多行语句的编写
total=['姓名','身份证',
       '录取学校','总分']
print(total)


#4. 数字（Number）类型
##整数型（int），在python3中没有Long定义长整型，系统默认长整型
##布尔型（bool），如True  #逻辑判断应该是常用的
##浮点数（float），如1.23，3E-2
##复数（complex），如1+2j，1.1+2.2j


#5. 字符串
'''
与其他语言不太一样的是，Python的单引号与双引号使用是完全一样的；
C语言里我记得''里面只能填一个字符，""里填的是字符串；若错误请批评指正。
'''
##在转义字符\之前加一个r可以让\不发生转义
##字符串运算，用+代表串联、*代表重复
##索引方式（略）
'''
Python中的字符串不能改变，这个与其他语言有点不一样，
其他C、MATLAB应该是可以通过赋值改变字符串
'''
##字符串切片str[start:end]，读取的区间你可以理解为左闭右开区间（[start,end)）
'''
步长的语法格式：str[start:end:step]
其他一般语言的语法格式是：str[start:step:end] 比如MATLAB
'''
##实例一
str='123456789' #定义字符串

print(str) #打印字符串
print(str[0:-1]) #输出第一个到倒数第二个的所有字符
print(str[0])#输出第一个字符
print(str[2:5])#输出从第三个到第六个字符（不包含第六个字符）
print(str[2:])#输出从第三个开始后的所有字符
print(str[1:5:2])#输出从第二个开始到第五个且每隔一个的字符（step=2）
print(str*2)#重复两次字符串
print(str+'你好')#串联字符串

print('---')

print('hello\nrunoob')#换行
print(r'hello\nrunoob')#使用r取消转义


#6. 空行
'''
也是程序代码的一部分，不是语法的一部分。
其作用是增强可读性，便于代码维护或者重构
'''


#7. 用户自行键入
##实例：
input("\n\n按下enter键后退出。")


#8. 同一行显示多余的语句--用;隔开
##实例一
import sys;x='runoob';sys.stdout.write(x+'\n')


#9. 多个语句构成代码组--缩进

#10.print输出
'''
print默认输出是换行的，如果要实现不换行要在变量末尾加end"":
'''
#实例一
x='a'
y='b'
print(x);print(y)#换行输出
print('---')
print(x,end="");print(y,end="");print()

#11. import与from...import
'''
常见的导入模块的格式我不写了，在这里我写一些不常用的格式：
从某个模块中导入多个函数：from somemodule import firstfunc,secondfunc,...
将某个模块全部函数导入：from somemodule import*
注：不明白发明这个格式有什么意义，直接import somemodule不就好了...
'''
##导入sys模块
import sys
print('==Python import mode==')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python的路径为',sys.path)

##导入sys模块的argv,path成员
from sys import argv,path
print('==python from import==')
print('path:',path)
'''
到这里我明白了那个格式的意义，如果不用那个格式，调用成员的时候要用这样的形式：
somemodule.Function
如果用了那个格式，直接用：
Function
就可以了
'''

#12.命令行参数（不太重要）




















