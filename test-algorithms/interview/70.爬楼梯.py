#
# @lc app=leetcode.cn id=70 lang=python
#
# [70] 爬楼梯
#
# https://leetcode.cn/problems/climbing-stairs/description/
#
# algorithms
# Easy (54.06%)
# Likes:    2916
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2M
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 2
# 输出：2
# 解释：有两种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶
# 2. 2 阶
# 
# 示例 2：
# 
# 
# 输入：n = 3
# 输出：3
# 解释：有三种方法可以爬到楼顶。
# 1. 1 阶 + 1 阶 + 1 阶
# 2. 1 阶 + 2 阶
# 3. 2 阶 + 1 阶
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 45
# 
# 
#

# @lc code=start
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """动态规划"""
        
        if n <= 2:
            return n

        dp = [0 for _ in range(n + 1)]
        dp[1], dp[2] = 1, 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]
# @lc code=end

