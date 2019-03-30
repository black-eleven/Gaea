# -*- coding: utf-8 -*-

def heapify(nums, start, end):
    # 左节点
    j = start*2 + 1
    father = start
    while j < end:
        if j+1 < end and nums[j] < nums[j+1]:
            j+=1
        if nums[father] > nums[j]:
            break
        nums[father], nums[j] = nums[j], nums[father]
        father = j
        j = 2*father + 1

def build_heap(nums):
    for i in range(len(nums)/2-1, -1, -1):
        heapify(nums, i, len(nums))

def heap_sort(nums):
    build_heap(nums)
    for i in range(len(nums)-1, -1, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, 0, i)

if __name__ == "__main__":
    l = [21, 25, 49, 25, 16, 8]
    #l = [5, 2, 9, 4, 7, 6, 1, 3, 8]
    #l = [1]
    #l = [2, 1]
    #l = []
    heap_sort(l)
    print l
