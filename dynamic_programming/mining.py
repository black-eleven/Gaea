# -*- coding: utf-8 -*-

# 有一个国家发现了5座金矿，每座金矿的黄金储量不同，需要参与挖掘的工人数也不同。参与挖矿工人的总数是10人（第二集说的是1000人，这里改动一下）。每座金矿要么全挖，要么不挖，不能派出一半人挖取一半金矿。要求用程序求解出，要想得到尽可能多的黄金，应该选择挖取哪几座金矿？


class Solution1(object):
    # 递归法
    def mining(self, golds, persons, t_person):
        if t_person == 0:
            return 0
        if len(persons) == 1:
            if persons[0] <= t_person:
                return golds[0]
            else:
                return 0
        last_not_mining = self.mining(golds[:-1], persons[:-1], t_person)
        if t_person - persons[-1] >= 0:
            last_mining = self.mining(golds[:-1], persons[:-1], t_person-persons[-1]) + golds[-1]
            return max(last_mining, last_not_mining)
        else:
            return last_not_mining

class Solution(object):
    # 动态规划
    def mining(self, golds, persons, t_person):
        dp = []
        for i in range(len(golds)):
            dp.append([])
            for j in range(t_person):
                dp[i].append(0)

        for i in range(len(golds)):
            for p in range(t_person):
                if p >= persons[i] and i-1 >= 0:
                    dp[i][p] = max(golds[i]+dp[i-1][p-persons[i]], dp[i-1][p])
                elif i == 0 and p >= persons[i]:
                    dp[i][p] = golds[i]
        print dp

if __name__ == "__main__":
    s = Solution()
    print s.mining([500, 200, 300, 350, 400], [5, 3, 4, 3, 5], 10)
