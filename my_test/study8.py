# /usr/bin/env python
# coding:utf-8

'''
异常：错误发生的信号，程序随之终止
三个部分：
    1.traceback 异常的追踪信息（链接）
    2.异常的类型
    3.异常信息
错误两大类：
    1.语法错误（运行前进行判定和修正）
    2.逻辑错误
异常种类：
    AttributeError 属性错误
        试图访问一个对象没有的树形，比如foo.x，但是foo没有属性x
    IOError 输出错误
        输入/输出异常；基本上是无法打开文件
    ImportError 模块导入错误
        无法引入模块或包；基本上是路径问题或名称错误
    IndentationError 缩进错误
        语法错误（的子类） ；代码没有正确对齐
    IndexError 索引错误
        下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
    KeyError 关键字错误
        试图访问字典里不存在的键
    KeyboardInterrupt 键盘中断错误
        Ctrl+C被按下
    NameError 名称错误
        使用一个还未被赋予对象的变量
    SyntaxError 语法错误
        Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
    TypeError 类型错误
        传入对象类型与要求的不符合
    UnboundLocalError 局部变量错误
        试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
    ValueError 值错误
        传入一个调用者不期望的值，即使值的类型是正确的
异常处理：
    #基本语法为
    try:
        被检测的代码块
    except 异常类型 as 别名： #别名用来去除异常的值
        try中一旦检测到异常后，执行的代码块。
    else：
        没有异常时执行
    finally：
        无论异常与否,都会执行该模块,通常是进行清理工作
    try：
        代码块1
        代码块2
        ……
    except StopIteration:
        代码块
        ……
    else：
        代码块
        ……
    finally：
        代码块
        ……
断言：assert 条件语句
    如果满足断言条件，继续运行；如果不满足，抛出异常(AssertionError)
'''
'''
# 1.指定异常捕捉（单分支）
try:
    print('========>1')
    print('========>2')
    l = [1, 2, 3]
    l[100]  # IndexError
    # 异常被捕捉，不执行try下后续代码块
    print('========>3')
    d = {'x': 1, 'y': 2}
    d['z']  # KeyError
    print('========>4')
except IndexError as ie:
    print('IndexError', ie)

print('other code')

# 2.异常处理多分支
try:
    print('========>1')
    print('========>2')
    d = {'x': 1, 'y': 2}
    d['z']  # KeyError

    print('========>3')
    l = [1, 2, 3]
    l[100]  # IndexError
    print('========>4')

except IndexError as ie:
    print('IndexError', ie)
except KeyError as ke:
    print('KeyError', ke)
# 同上
except (IndexError, KeyError) as e:
    print('Error', e)

print('other code')

# 3.万能异常 Exception：可以匹配任意类型的异常
try:
    print('========>1')
    print('========>2')
    d = {'x': 1, 'y': 2}
    d['z']  # KeyError

    print('========>3')
    l = [1, 2, 3]
    l[100]  # IndexError
    print('========>4')

except Exception as e:
    print('Error', e)

print('other code')

# 4.万能异常+多分支，实现指定错误指定处理。即：万能异常放最后捕获
try:
    print('========>1')
    print('========>2')
    d = {'x': 1, 'y': 2}
    d['z']  # KeyError

    print('========>3')
    l = [1, 2, 3]
    l[100]  # IndexError
    print('========>4')

except IndexError as ie:
    print('IndexError', ie)
except KeyError as ke:
    print('KeyError', ke)
except Exception as e:
    print('Error', e)

print('other code')

# 5.else和finally的使用和区别
try:
    print('========>1')
    print('========>2')
    d = {'x': 1, 'y': 2}
    d['z']  # KeyError

    print('========>3')
    l = [1, 2, 3]
    l[100]  # IndexError
    print('========>4')

except IndexError as ie:
    print('IndexError', ie)
except KeyError as ke:
    print('KeyError', ke)
except Exception as e:
    print('Error', e)
else:
    print('else')
finally:
    print('finally')

print('other code')

# 6.主动抛出异常
raise TypeError('类型错误')

# 7.触发异常
try:
    raise TypeError('类型错误')
except Exception as e:
    print(e)


# 8.自定义异常
class MyException(BaseException):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    raise MyException('类型错误')
except MyException as me:
    print(me)

# 断言：assert 条件语句
# 如果满足断言条件，继续运行；如果不满足，抛出异常(AssertionError)
print('1111')
l = [1, 2, 3, ]
assert len(l) > 5
print('22222222')


# 捕获异常
class People:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_interface(self):
        print(self.__name, self.__age)

    def set_inter(self, name, age):
        try:
            if not isinstance(name, str):
                raise TypeError('名字必须是str类型')
            if not isinstance(age, int):
                raise TypeError('年龄必须是int类型')
        except TypeError as te:
            print(te)
            return te
        self.__name = name
        self.__age = age


p1 = People(100, 100)
p1.get_interface()

p1.set_inter(110, 101)
p1.get_interface()

p1.set_inter('name1', 'age1')
p1.get_interface()

p1.set_inter('name2', 19)
p1.get_interface()

'''