# -*- coding: utf-8 -*-

def merge(nums, left, mid, right):
    tmp = []
    i, j = left, mid
    while i < mid and j < right:
        if nums[i] < nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    while i < mid:
        tmp.append(nums[i])
        i += 1
    while j < right:
        tmp.append(nums[j])
        j += 1
    nums[left:right] = tmp[:]

def merge_sort_recursion(nums, left, right):
    if right - left <= 1:
        return
    mid = (left+right)/2
    merge_sort_recursion(nums, left, mid)
    merge_sort_recursion(nums, mid, right)
    merge(nums, left, mid, right)

def merge_sort_iteration(nums):
    i = 1
    while i < len(nums):
        j = 0
        while j < len(nums)-i:
            mid = j + i
            right = mid+i if mid + i < len(nums) else len(nums)
            merge(nums, j, mid, right)
            j = right
        i = i*2

if __name__ == "__main__":
    l = [21, 25, 49, 25, 16, 8]
    l = [5, 2, 9, 4, 7, 6, 1, 3, 8]
    # l = [1]
    # l = [2, 1]
    # l = []
    #merge_sort_recursion(l, 0, len(l))
    merge_sort_iteration(l)
    print l
