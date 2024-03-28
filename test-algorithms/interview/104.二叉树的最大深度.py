#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#
# https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (77.36%)
# Likes:    1786
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 1.6M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树 root ，返回其最大深度。
# 
# 二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
# 
# 
# 
# 示例 1：
# 
# 
# 
# 
# 
# 
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,null,2]
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数量在 [0, 10^4] 区间内。
# -100 <= Node.val <= 100
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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        算法解析：
            终止条件： 当 root​ 为空，说明已越过叶节点，因此返回 深度 0 。
            递推工作： 本质上是对树做后序遍历。
                计算节点 root​ 的 左子树的深度 ，即调用 maxDepth(root.left)。
                计算节点 root​ 的 右子树的深度 ，即调用 maxDepth(root.right)。
            返回值： 返回 此树的深度 ，即 max(maxDepth(root.left), maxDepth(root.right)) + 1。

        """
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
# @lc code=end

