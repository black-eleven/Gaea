# -*- coding: utf-8 -*-

# 你正在爬楼梯。 它需要n步才能达到顶峰。
# 每次你可以爬1或2步。 您可以通过多少不同的方式登顶？
#
# 注意：给定n将是一个正整数。

# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution1(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one_step = 1
        two_step = 0
        for i in range(n-1):
            tmp = one_step
            one_step = one_step + two_step
            two_step = tmp
        return one_step + two_step

if __name__ == "__main__":
    s = Solution()
    print s.climbStairs(6)
