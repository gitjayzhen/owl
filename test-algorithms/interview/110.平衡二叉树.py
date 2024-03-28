#
# @lc app=leetcode.cn id=110 lang=python
#
# [110] 平衡二叉树
#
# https://leetcode.cn/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (58.14%)
# Likes:    1487
# Dislikes: 0
# Total Accepted:    584.5K
# Total Submissions: 1M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：root = []
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 树中的节点数在范围 [0, 5000] 内
# -10^4 
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        def helper(root):
            if root is None:
                return 0
            return max(helper(root.left), helper(root.right)) + 1
        return abs(helper(root.left) - helper(root.right)) <= 1 \
                and self.isBalanced(root.left) \
                and self.isBalanced(root.right)
        
# @lc code=end

