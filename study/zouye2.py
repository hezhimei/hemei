# /usr/bin/env python
# coding:utf-8
'''
list = []
for i in range(1000,2500):
    if i%7 == 0 and i%5 == 0:
        list.append(i)
    else:
        continue
print(list)
'''
for i in range(21):
    if i%3 == 0 and i%5 == 0:
        print("threes+five")
    elif i%3 == 0:
        print("threes")
    elif i%5 == 0:
        print("fives")
    else:
        print(i)
    continue


