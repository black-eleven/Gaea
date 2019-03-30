# -*- coding: utf-8 -*-

def search_rotated_list(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left+right)/2
        if nums[mid] == target:
            return mid
        if nums[mid] < nums[left]:
            # 说明拐点在左边
            if nums[mid] < target and nums[right] >= target:
                left = mid + 1
            else:
                right = mid - 1
        elif nums[mid] > nums[right]:
            # 说明拐点在右边
            if nums[mid] > target and nums[left] <= target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return -1

if __name__ == "__main__":
    #print search_rotated_list([4,5,6,7,0,1,2], 0)
    print search_rotated_list([3,5,1], 3)
