# -*- coding: utf-8 -*-

# 给定非负整数num。 对于范围0≤i≤num中的每个数字i，计算其二进制表示中的1的数量并将它们作为数组返回。
#
# 例1：
#
# 输入：2
# 输出：[0,1,1]
# 例2：
#
# 输入：5
# 输出：[0,1,1,2,1,2]
# 跟进：
#
# 很容易想出一个运行时间为O（n * sizeof（整数））的解决方案。 但你可以在线性时间O（n）/可能在一次通过吗？
# 空间复杂度应为O（n）。

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        dp = [0, 1] + [None] * (num-1)
        div = 1
        for i in range(2, num+1):
            if i >= div*2:
                div = div * 2
            dp[i] = dp[i%div] + dp[i/div]
        return dp

if __name__ == "__main__":
    s = Solution()
    print s.countBits(2)
