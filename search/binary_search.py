# -*- coding: utf-8 -*-

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left+right)/2
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1

if __name__ == "__main__":
    print binary_search([1, 3, 5, 7, 9], 9)
