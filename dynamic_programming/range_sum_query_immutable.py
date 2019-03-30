# -*- coding: utf-8 -*-

# 给定整数数组nums，找到索引i和j（i≤j）之间的元素之和，包括端点。
#
# 例：
# 给定nums = [-2,0,3，-5,2，-1]
#
# sumRange（0,2） - > 1
# sumRange（2,5） - > -1
# sumRange（0,5） - > -3
#
# 注意：
# 您可以假设阵列不会更改。
# sumRange函数有很多调用。

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return
        self.sums = [nums[0]]
        for i in range(1, len(nums)):
            self.sums.append(self.sums[i-1] + nums[i])

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j] - (self.sums[i-1] if i > 0 else 0)

if __name__ == "__main__":
    obj = NumArray([-2, 0, 3, -5, 2, -1])
    print obj.sumRange(0, 2)
    print obj.sumRange(2, 5)
    print obj.sumRange(0, 5)
