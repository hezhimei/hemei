# /usr/bin/env python
# coding:utf-8


def sum_func(lists):
    sum = 0
    for i in lists:

        if str(i).isdecimal() == True:
            sum += i
        else:
            continue
    print(sum)


#sum_func([1,2,3])
#sum_func([1,2,4,'a'])


dic={"name":"xiaozhang","sex":"male"}
def dic_func(key):
    try:
        print(dic[key])
    except KeyError as ie:
        print('KeyError',ie)

dic_func("grade")


def flexible(aa,*args,**kwargs):
    aa = 1
    print(args)
    print(kwargs)

flexible('aa',2,3,x=4,y=5,*[1,2,3],**{'a':1,'b':2})

try:
    file_in = open("../study/study6.py","r")
    content = file_in.read()
    print(content)
except IOError as ie:
    print('IOError',ie)

