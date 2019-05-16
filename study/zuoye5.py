# /usr/bin/env python
# coding:utf-8
from study.zuoye4 import Server

class Price(Server):

    def __init__(self,num,size1,size2,sys1):
        Server.__init__(self,num,size1,size2,sys1)


    def get_price(self):
        # price = Server.get_num(self)*1527.679+Server.get_size1(self)*100.21+Server.get_size2(self)*50.789
        self.price = 1527*self.num+100.21*self.size1+50.789*self.size2
        return self.price



    #def set_price(self,price=None):
         #self.price=1527*self.num+100.21*self.size1+50.789*self.size2


if __name__=="__main__":
    # price = Server(8,40,150,'Linux')
    # print(Price.get_price())
    price = Price(8,40,150,'linux')
    print(round(price.get_price(),2))



