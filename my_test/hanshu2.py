# /usr/bin/env python
# coding:utf-8

class Person:       #没有构造函数

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name=name

if __name__=="__main__":
    per1=Person()
    per1.set_name("hanmeimei")
    print(per1.get_name())