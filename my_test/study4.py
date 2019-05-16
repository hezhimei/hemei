# /usr/bin/env python
# coding:utf-8

#数据处理-列表

#主要方法：长度，增删改查，反转，排序
book = ['python','java','appium','selenium']
print(book[1])          #输出列表中第二个数
print(len(book))
book.append('c++')      #追加
book.pop()  #弹出最后一个数
book.pop(2)    #删除第3个数据
book.insert(2,'ddd')    #将数据插入第3位置
book1 = ['a','b']
book.extend(book1)      #在列表后面追加另一个列表
print(book)
book.remove("b")        #在列表中删除一个指定项
book.reverse()          #反转
book.sort()             #排序
book.copy()             #复制
book.copy()*4            #拷贝4遍
book.clear()             #全部删除





