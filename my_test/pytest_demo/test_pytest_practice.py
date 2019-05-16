# /usr/bin/env python
# coding:utf-8

import random
import pytest
import time




def bubble_sort(nums):
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    #return nums
    return random.choice([nums,None,10])


@pytest.mark.parametrize('nums',[([4,2,5,9,1])])
def test_bubble_sort(nums):
    assert bubble_sort(nums) == [1, 2, 4, 5, 9]


def test_bubble_sort1(nums):
    time.sleep(1)
    assert bubble_sort(nums) is  None

def test_bubble_sort2(nums):
    time.sleep(2)
    assert bubble_sort(nums) == 10

