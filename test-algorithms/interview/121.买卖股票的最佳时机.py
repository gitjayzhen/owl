#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (57.71%)
# Likes:    3420
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 2.3M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
# 
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
# ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
# 
# 
# 示例 2：
# 
# 
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 0 
# 
# 
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        
        [7,1,5,3,6,4]
        
          -6 4 -2 3 -2
        
        1. 记录最小的成本
        2. 找到后续价格减去最小成本的值，求最大即可
        """

        # if len(prices) <= 1:
        #     return 0
        # max_v = prices[1] - prices[0]
        # index = 1
        # for i in range(1, len(prices)):
        #     v = prices[i] - prices[i-1]
        #     if v + max_v > max_v:
        #         index = i
        #         max_v = v
        # return max_v
    
        cost, profit = float('+inf'), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
        
# @lc code=end

