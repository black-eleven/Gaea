# -*- coding: utf-8 -*-

def insert_sort_binary(nums):
    for i in range(len(nums)):
        left = 0
        right = i - 1
        tmp = nums[i]
        while left <= right:
            mid = (left+right)/2
            if nums[mid] > tmp:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i-1, left-1, -1):
            nums[j+1] = nums[j]
        nums[left] = tmp

if __name__ == "__main__":
    l = [21, 25, 49, 25, 16, 8]
    #l = [5, 2, 9, 4, 7, 6, 1, 3, 8]
    insert_sort_binary(l)
    print l
