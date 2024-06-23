#2_基本数据类型

#1. 简单的赋值
counter=100 #整型变量
miles=1000.0 #浮点型变量
name= "runoob" #字符串

print(counter)
print(miles)
print(name)


#2. 多个变量赋值
a=b=c=1 #同时赋一个相同的值
a,b,c=1,2,"runoob"#同时赋不同的值，且数据类型可以不同


#3. 标准数据类型
'''
常见的数据类型
Number（数字）、String(字符串)、bool(布尔类型)
List(列表)、Tuple(元组)、Set(集合)
Dictionary（字典）
不可变数据：Number（数字）、String(字符串)、Tuple(元组)；
可变数据：List(列表)、Dictionary（字典）、Set(集合)。
高级数据类型：字节数组（bytes）
'''
#4.Number(数字)
#支持：int、float、bool、complex（复数）
#type（）：查询变量所指的对象类型
#实例：
a=111 #赋值为int型数据
isinstance(a,int)#isinstance(variable,class)判断变量variable是不是class类型

'''
isinstance 和 type 的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
'''
#bool是int的子类
#实例：变量运算
5+4
4.3-2
3*7
2/4 #除法，得到一个浮点数
2//4#除法，得到一个整数
17%3 #取余
2**5 #乘方（取幂）


#5. String（字符串）
#实例一：字符串赋值、读取
str='Runoob' #定义一个字符串变量

print(str) #打印整个字符串
print(str[0:-1]) #打印字符串第一个到倒数第二个字符（不包含倒数第一个字符）
print(str[0]) # 打印字符串的第一个字符
print(str[2:5])# 打印字符串第三到第五个字符（包含第五个字符）
print(str[2:])# 打印字符串从第三个字符开始到末尾
print(str*2) # 打印字符串两次
print(str+"TEST") #串联字符串

#实例二：用反斜杠（\)转义特殊字符，用r取消转义
print('Ru\noob')
print(r'Ru\noob')
#PS：反斜杠（\）可以作为续行符

#实例三：打印字符串中的某个元素
word='Python'
print(word[0],word[5])
print(word[-1],word[-6])
#PS：字符串定义之后就无法通过赋值来改变了


#6. bool（布尔类型）
#实例：比较运算符、逻辑运算符、类型转换
a=True
b=False

#比较运算符
print(2<3)
print(2==3)

#逻辑运算符
print(a and b)
print(a or b)
print(not a)

#类型转换
print(int(a))
print(float(b))
print(a)


#7. List(列表)
#实例一：列表的创建与打印
list=['abcd',786,2.23,'runoob',70.2] #定义一个列表

tinylist=[123,'runoob'] #定义一个小列表

print(list) # 打印整个列表
print(list[0]) # 打印列表的第一个元素
print(list[1:3])# 打印列表第二到第四个元素（不包含第四个元素）
print(list[2:])# 打印列表从第三个元素开始到末尾
print(tinylist)#打印tinylist列表两次
print(list+tinylist) #串联两个列表
#PS：列表的元素是可以改变的

#实例二：翻转字符串
def reverseWords(input):
    #通过空格将字符串分隔符，把各个单词分隔为列表
    inputWords=input.split(" ")
    #翻转字符串
    #假设列表list=[1,2,3,4]
    #inputWords[-1::-1]有三个参数
    #第一个参数-1表示最后一个元素
    #第二个参数为空，表示移动到列表末尾
    #第三个参数为步长，-1表示逆向
    inputWords=inputWords[-1::-1]

    #重新组合字符串
    output=' '.join(inputWords)

    return output

if __name__=="__main__":
    input='I like runoob'
    rw=reverseWords(input)
    print(rw)


#8. Tuple（元组）
#实例一：元组的创建与打印
tuple=('abcd',786,2.23,'unoob',70.2)
tinytuple=(123,'runoob')

print(tuple) #输出完整元组
print(tuple[0]) #输出元组的第一个元素
print(tuple[1:3])#输出从第二个元素到第三个元素
print(tuple[2:])#输出从第三个元素开始的所有元素
print(tinytuple*2)#输出两次元组
print(tuple+tinytuple) #连接元组
#PS:可以把字符串看作是一个特殊的元组


#9. Set(集合)
#创建格式：
'''
parame={value01,value02,...}
或者
set(value)
'''
#实例：集合的创建、成员测试、集合运算
sites={'Google','Taobao','Runoob','Facebook','Zhihu','Baidu'}

print(sites) #输出集合，重复的元素会被自动去掉

#成员测试
if 'Runoob' in sites:
    print('在哦')
else:
    print('不在的哟')

#集合运算
a=set('abcdefg')
b=set('acdf')

print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b) #a与b中不同时存在的元素


#10. Dictionary（字典）
#实例一：字典的创建与输出
dict={}
dict['one']="1-菜鸟教程"
dict[2]="2-菜鸟工具"

tinydict={'name':'runoob','code':1,'site':'www.runoob.com'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
#构造函数dict()可以直接从键值对序列中构建字典，如下
#实例二：运用函数dict()构建字典
'''
dict([('Runoob',1),('Google',2),('Taobao',3)])
{x:x**2 for x in (2,4,6)}
dict(Runoob=1,Google=2,Taobao=3)
#PS:*2 for x in(2,4,6)}用的是字典推导式 ，目前没学

'''
#11. bytes类型
#实例一：bytes对象的创建
x=b"hello"
y=x[1:3] #切片操作 得到b"el"
z=x+b"world" #拼接操作，得到b"helloworld"
print(x)
print(y)
print(z)

#实例二：bytes类型的元素——整数值
x=b"hello"
if x[0]==ord('h'):
    print("The first element is 'h'")
#PS：ord()用于将字符转换为对应的整数值
















          
