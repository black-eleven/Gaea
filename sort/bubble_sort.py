# -*- coding: utf-8 -*-

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]

def bubble_sort_1(nums):
    for i in range(len(nums)-1):
        for j in range(0, len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

if __name__ == "__main__":
    l = [16, 8, 21, 25, 49, 25]
    #l = [5, 2, 9, 4, 7, 6, 1, 3, 8]
    l = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    bubble_sort_1(l)
    print l
