# /usr/bin/env python
# coding:utf-8
#while循环
'''
n = 1
count = 0
while n <= 10:
    count += n
    n +=1
print(count)


#for循环
lis1 = [1,2,3,4,5,6,7,8,9,10]
count = 0
for i in lis1:
    count =count + i
print(count)


count = 0
for i in range(11):
    count += i
print(count)

'''
'''
循环的中断
break  跳出整个循环
continue  跳出本次循环，继续执行下一次循环
'''
#while True:
   # print(1)
    #break
    #print(2)


#while True:
    #print(1)
    #continue
    #print(2)

'''
1、冒泡排序

'''
'''
nums = [3,1,25,16,18,7,8]
for i in range(len(nums)-1):
    for j in range(len(nums)-i -1):
        if nums[j] > nums[j+1]:
            nums[j],nums[j + 1] = nums[j + 1],nums[j]
        print("第"+str(j) + "次内循环" + str(nums))
    print("第"+ str(j) + "次外循环" + str(nums))
print("最后的结果" + str(nums))
'''
'''
作业：
已经有一个序列
将序列从大到小排序
申明一个变量数字，i=7，将i插入到序列中，他应该在的大小的位置
思路提示：
重新申明一个新的序列，然后拿第一个序列中的值跟i比较，比i大的可以直接放入序列中，比i小的
先放i，然后再放七天的值
'''

nums = [4,2,19,25,8,10,13]
for a in range(len(nums)- 1):
    for b in range(len(nums)-a -1):
        if nums[b] < nums[b+1]:
            nums[b],nums[b+1] = nums[b+1],nums[b]
print(nums)
i = 7
nums1 = nums + [7]
print(nums1)
for c in range(len(nums)):
    if nums[len(nums)-c-1] < nums1[len(nums)-c]:
       nums1[len(nums)-c-1],nums1[len(nums)-c] = nums1[len(nums)-c],nums1[len(nums)-c-1]

print(nums1)
print(nums1.index(7))




