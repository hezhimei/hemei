# /usr/bin/env python
# coding:utf-8
'''

first_num = input ("请输入第一个数字：")
operation = input ("请输入运算符：")
second_num = input ("请输入第二个数字：")

print(type(first_num))

if '.' not in (first_num and second_num):
    first_num = int(first_num)
    second_num = int(second_num)


else :
    first_num = float(first_num)
    second_num = float(second_num)
if operation == "+":
    result = first_num + second_num
elif operation == "-":
    result = first_num - second_num
elif operation == "*":
    result = first_num * second_num
elif operation == "/":
    result = first_num / second_num
#result = str(result)
print ( "计算结果为：" , result)

'''
a = float(input("数字1："))
b = input("符号：")
c = float(input("数字2："))
if b == "+":
    A = a+c
elif b == "-":
    A = a-c
elif b == "*":
    A = a*c
elif b == "/":
    A = a/c
B = int(A)
C = A-B
if ( C == 0 ):
    print(B)
else:
    print(A)

