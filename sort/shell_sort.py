# -*- coding: utf-8 -*-

def shell_sort(nums):
    h = len(nums)
    while h > 1:
        h = h/3 + 1
        for i in range(h, len(nums)):
            j = i - h
            tmp = nums[i]
            while j >= 0 and nums[j] > tmp:
                nums[j+h] = nums[j]
                j-=h
            nums[j+h] = tmp
        print 'h: ', h, ', nums: ', nums

if __name__ == "__main__":
    l = [21, 25, 49, 25, 16, 8]
    # l = [5, 2, 9, 4, 7, 6, 1, 3, 8]
    # l = [1]
    # l = [2, 1]
    # l = []
    shell_sort(l)
    print l
