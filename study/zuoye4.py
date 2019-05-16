# /usr/bin/env python
# coding:utf-8

class Server:
    def __init__(self,num,size1,size2,sys1):

        self.num = num
        self.size1 = size1
        self.size2 = size2
        self._sys1 = sys1


    def get_num(self):
        return str(self.num)+"核CPU"

    def get_size1(self):
        return str(self.size1) +"G内存"

    def get_size2(self):
        return str(self.size2) + "G磁盘空间"
        #print(str(self.size2)+"g磁盘")

    def get_sys1(self):
        return self._sys1
'''
    def get_sys1(self):
        if self._sys1 =='Linux' or self._sys1=='Windows':
            return self._sys1
        else:
            print("请输入正确的系统类型")

    def set_sys1(self,sys1):
        self._sys1 = sys1


'''




if __name__=="__main__":
    server1 =Server (8,40,150,'Linux')
    print(server1.get_num(),server1.get_size1(),server1.get_size2(),server1._sys1)
