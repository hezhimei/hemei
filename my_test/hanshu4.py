# /usr/bin/env python
# coding:utf-8

#多重继承
from my_test.hanshu3 import Student

class StudentSenior(Student):

    def __init__(self,name,sex,province,grade):
        Student.__init__(self,name,sex,province,grade)

    def get_province(self):
        return self.province

    def get_name(self):
        name=Student.get_name(self)
        return name

    def overtime_study(self):
        if self.grade==3:
            return "补课"
        else:
            return "不补课"
if __name__=="__main__":
    ss=StudentSenior("apple","Female","zhejiang",3)
    print(ss.overtime_study())
    print(ss.grade)
    print(ss.name)
    print("*"*20)
    print(ss.province)
    print(ss.sex)


