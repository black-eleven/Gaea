# -*- coding: utf-8 -*-
import sys

# 假设您有一个数组，其中第i个元素是第i天给定股票的价格。
# 如果您只被允许完成最多一笔交易（即买入并卖出一股股票），请设计算法以找到最大利润。
# 请注意，在购买之前不能出售股票。

# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5

# Example 2:
#
# Input: [7,6,4,3,1]
# Output: 0

class Solution1(object):
    # 缺点是用的空间过多
    # 这是个自顶向下的过程
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        price = (max(prices[1:]) if len(prices)>1 else 0) - prices[0]
        return max(self.maxProfit(prices[1:]), price)

class Solution(object):
    # 真正的动态规划是一个自底向上的过程求解，以得到较好的时间空间复杂度
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit, min_price = 0, sys.maxint
        for p in prices:
            profit = p - min_price
            max_profit = max(profit, max_profit)
            min_price = min(p, min_price)
        return max_profit

if __name__ == "__main__":
    s = Solution()
    print s.maxProfit([7,1,5,3,6,4])
    print s.maxProfit([7,6,4,3,1])
