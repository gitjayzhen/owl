#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#
# https://leetcode.cn/problems/symmetric-tree/description/
#
# algorithms
# Easy (59.78%)
# Likes:    2662
# Dislikes: 0
# Total Accepted:    991K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
# 
# 
# 
# 
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root,root)
    
    def isMirror(self, root1, root2):
        if root1 is None or root2 is None:
            return root2 == root1
        return (root1.val == root2.val) and \
        self.isMirror(root1.left, root2.right) and \
        self.isMirror(root1.right, root2.left)
# @lc code=end

