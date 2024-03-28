#
# @lc app=leetcode.cn id=35 lang=python
#
# [35] 搜索插入位置
#
# https://leetcode.cn/problems/search-insert-position/description/
#
# test-algorithms
# Easy (45.16%)
# Likes:    1643
# Dislikes: 0
# Total Accepted:    884.6K
# Total Submissions: 2M
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 请必须使用时间复杂度为 O(log n) 的算法。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums 为 无重复元素 的 升序 排列数组
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        二分查找
        """
        # 取的是左右两边的下标
        left, right = 0, len(nums) - 1
        # 终止计算
        while left <= right:
            # 找到中间位置的元素，使用整除
            mid = (left + right) // 2
            # 由中间位置来判定向左向右偏移
            if nums[mid] >= target:
                # 中间这个位置的值比目标值要大，所以这个数据不用在进行比较，向左偏移
                right = mid - 1
            else:
                left = mid + 1
        return left


# @lc code=end

