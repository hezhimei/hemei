# /usr/bin/env python
# coding:utf-8


class Person:
    total_person=0     #类变量  访问需要 类名.类变量 访问，在多个实例中共享数据
    def __init__(self,name,sex,province,weight):    #构造函数初始化
        print("Init the class")
        self.name=name          #实例变量访问方法，实例变量只作用在此实例中
        self.sex=sex
        self.province=province
        self._weight = weight
        Person.total_person+=1     #类变量访问方法

'''
    @staticmethod
    def set_new_name(new_name):
        return "new name is:"+new_name

    @classmethod
    def set_new_province(cls,new_province):
        return "Your province is:"+new_province

    @property
    def get_sex(self):
        return self.sex
'''
#实例变量的另一种访问方法
'''
    def get_name(self):
        return self.name

    def get_sex(self):
        return self.sex
'''
if __name__=="__main__":
    person3 = Person("xiaozhang","Male","Beijing",60)

    #print(person3.set_new_name("hanmeimei"))
    #print(person3.set_new_province("zhejiang"))
    #print(person3.get_sex)
    print(person3.sex)
    print(person3._weight)


'''
    person1 = Person("xiaozhang","Male","Beijing",60)    #类的初始化（实例化）
    print(person1.sex)
    print(person1.name)
    print(person1.get_sex)
   # print(person1.get_sex())
    print(person1.total_person)

    person2 = Person("Hanmeimei","Female","Shanghai",60)
    print(person2.sex)
    print(person2.name)
    print(person2.total_person)
'''
