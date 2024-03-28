#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子数组和
#
# https://leetcode.cn/problems/maximum-subarray/description/
#
# test-algorithms
# Easy (54.76%)
# Likes:    5217
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 
# 子数组 是数组中的一个连续部分。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1]
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：nums = [5,4,-1,7,8]
# 输出：23
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 
# 
# 
# 
# 进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。
# 
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        动态规划 
        标准动态规划 dp[i] 定义为数组nums 中已num[i] 结尾的最大连续子串和， 
        则有dp[i] = max(dp[i-1] + nums[i], num[i]);
        
        """
        pre, count = 0, nums[0]
        
        for i in nums:
            pre = max(pre + i, i)
            # print(pre)
            count = max(pre, count)
        return count
            
# @lc code=end

