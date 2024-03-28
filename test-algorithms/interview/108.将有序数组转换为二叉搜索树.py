#
# @lc app=leetcode.cn id=108 lang=python
#
# [108] 将有序数组转换为二叉搜索树
#
# https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (78.10%)
# Likes:    1485
# Dislikes: 0
# Total Accepted:    438.4K
# Total Submissions: 561K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。
# 
# 高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
# 解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
# 
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,3]
# 输出：[3,1]
# 解释：[1,null,3] 和 [3,1] 都是高度平衡二叉搜索树。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^4
# -10^4 <= nums[i] <= 10^4
# nums 按 严格递增 顺序排列
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        
        树的中序遍历是升序的
        """
        
        def result_helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
        
            root = TreeNode(nums[mid])
            root.left = result_helper(left, mid - 1)
            root.right = result_helper(mid + 1, right)
            return root
        return result_helper(0, len(nums) - 1)
        
# @lc code=end

