# /usr/bin/env python
# coding:utf-8


import random


#@pytest.mark.parametrize([4,2,5,9,1])

def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return random.choice([nums,None,10])
    #return nums

print(bubble_sort([4,2,5,9,1]))


#def test_bubble_sort(nums):
    #assert bubble_sort(nums) ==