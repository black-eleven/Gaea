# -*- coding: utf-8 -*-

def selection_sort(nums):
    for i in range(len(nums)):
        min_location = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_location]:
                min_location = j
        if min_location != i:
            nums[min_location], nums[i] = nums[i], nums[min_location]

if __name__ == "__main__":
    l = [16, 8, 21, 25, 49, 25]
    #l = [5, 2, 9, 4, 7, 6, 1, 3, 8]
    selection_sort(l)
    print l
