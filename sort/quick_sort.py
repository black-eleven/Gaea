# -*- coding: utf-8 -*-

def quick_sort(nums, start, end):
    if start >= end:
        return
    i, j = start, end-1
    base = nums[start]
    while i < j:
        while i < j and nums[j] >= base:
            j-=1
        nums[i] = nums[j]
        while i < j and nums[i] <= base:
            i+=1
        nums[j] = nums[i]
    nums[i] = base
    quick_sort(nums, start, i)
    quick_sort(nums, j+1, end)

if __name__ == "__main__":
    l = [21, 25, 49, 25, 16, 8]
    #l = [5, 2, 9, 4, 7, 6, 1, 3, 8]
    #l = [1]
    #l = [2, 1]
    #l = []
    quick_sort(l, 0, len(l))
    print l
