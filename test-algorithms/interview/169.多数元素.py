#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#
# https://leetcode.cn/problems/majority-element/description/
#
# algorithms
# Easy (66.37%)
# Likes:    2166
# Dislikes: 0
# Total Accepted:    898.7K
# Total Submissions: 1.4M
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [3,2,3]
# 输出：3
# 
# 示例 2：
# 
# 
# 输入：nums = [2,2,1,1,1,2,2]
# 输出：2
# 
# 
# 
# 提示：
# 
# 
# n == nums.length
# 1 <= n <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
# 
# 
# 
# 
# 进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
# 
#

# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        三种解法：

        哈希表统计法： 遍历数组 nums ，用 HashMap 统计各数字的数量，即可找出 众数 。此方法时间和空间复杂度均为 O(N) 。
        数组排序法： 将数组 nums 排序，数组中点的元素 一定为众数。
        摩尔投票法： 核心理念为 票数正负抵消 。此方法时间和空间复杂度分别为 O(N) 和 O(1) ，为本题的最佳解法。
        """
        vote = 0
        result = 0
        for num in nums:
            if vote == 0:
                result = num
            vote += 1 if result == num else -1
        return result
            
        
# @lc code=end

