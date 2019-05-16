# /usr/bin/env python
# coding:utf-8

#单元测试的覆盖率
#语句覆盖（statement coverage)
#判断覆盖（decision coverage）
#条件覆盖（condition coverage）
#路径覆盖（path coverage）


def demo_method(a,b,x):

    if(a>1 and b==0):
        x=x/a

    if(a==2 or x>1):
        x=x+1
    return x

'''
1,语句覆盖：运行测试用例的过程中被击中的代码行即称为被覆盖的语句
测试用例：a=3,b=0,x=3
漏洞：如果将and改为or，无法判断出来这个漏洞

2.判断覆盖：运行测试用例的过程中被击中的判定语句
测试用例：
testcase  abx    a>1 and b==0    a==2 or x>1  executepath
1         203         t             t            135
2         101         f             f            124
3         303         t             f            134
4         211         f             t            125
漏洞：a==2 or x>1 => a==2 or x<1

3.条件覆盖：每一个判断覆盖语句中，每个可能的子条件或者合并条件都覆盖到

4.路径覆盖：每一个可能的路径都被覆盖到


'''