# /usr/bin/env python
# coding:utf-8

#函数
def hello_func(greeting,name='apple'):        #greeting是位置参数，name是关键字参数
    return '{} {} 你好.'.format(greeting,name)

print(hello_func('hi'))
print(hello_func('hi','tom'))

def student_info(*args,**kwargs):       #*args是不定长参数，**kwargs是字典型参数
    print(args)
    print(kwargs)


courses = ['python','java']
info = {'name':'apple','age':18}
student_info(courses,info)
student_info(*courses,**info)         #加*相当于解包了

def foo(x,*args,a=4,**kwargs):      #使用默认参数时，注意默认参数要在args之前
    print(x)
    print(a)
    print(args)
    print(kwargs)

foo(1,(5,6,7,8),{"y":2,"z":3})
foo(1,*(5,6,7,8),**{"y":2,"z":3},a=6)
foo(2,(5,6,7,8),y=2)



#匿名函数
add = lambda x,y:x+y
add1 = lambda *args: sum(args)
print(add1(1,56,25))
