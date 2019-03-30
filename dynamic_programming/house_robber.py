# -*- coding: utf-8 -*-

# 你是一个专业的强盗，计划在街上抢劫房屋。 每个房子都藏着一定数量的钱，阻止你抢劫他们的唯一限制因素是相邻的房屋有连接的安全系统，如果两个相邻的房子在同一个晚上被闯入，它将自动联系警方。

# 给出一个代表每个房子的金额的非负整数列表，确定今晚可以抢劫的最大金额而不警告警察。


# Example 1:
#
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4.

# Example 2:
#
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.

class Solution1(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        rob_cur = self.rob(nums[2:]) + nums[0]
        no_rob_cur = self.rob(nums[1:])
        return max(rob_cur, no_rob_cur)

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [nums[0], max(nums[0], nums[1])]
        max_rob = 0
        for i in range(2, len(nums)):
            rob_cur_max = nums[i] + max(dp[:i-1])
            no_rob_cur_max = max(dp[:i])
            dp.append(max(rob_cur_max, no_rob_cur_max))
        return dp.pop()

if __name__ == "__main__":
    s = Solution()
    print s.rob([1,2,3,1])
    print s.rob([2,7,9,3,1])
    print s.rob([1,3,1])
    print s.rob([2,1,1,2])
