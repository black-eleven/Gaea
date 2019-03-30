# -*- coding: utf-8 -*-

def insert_sort(nums):
    for i in range(len(nums)):
        j = i - 1
        tmp = nums[i]
        while j >= 0 and tmp < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = tmp

if __name__ == "__main__":
    #l = [16, 8, 21, 25, 49, 25]
    l = [5, 2, 9, 4, 7, 6, 1, 3, 8]
    insert_sort(l)
    print l
