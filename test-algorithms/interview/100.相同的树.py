#
# @lc app=leetcode.cn id=100 lang=python
#
# [100] 相同的树
#
# https://leetcode.cn/problems/same-tree/description/
#
# algorithms
# Easy (60.90%)
# Likes:    1135
# Dislikes: 0
# Total Accepted:    539.2K
# Total Submissions: 884.8K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# 给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。
# 
# 如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：p = [1,2,3], q = [1,2,3]
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：p = [1,2], q = [1,null,2]
# 输出：false
# 
# 
# 示例 3：
# 
# 
# 输入：p = [1,2,1], q = [1,1,2]
# 输出：false
# 
# 
# 
# 
# 提示：
# 
# 
# 两棵树上的节点数目都在范围 [0, 100] 内
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        
        深度优先搜索
        
        标签：深度优先遍历

            终止条件与返回值：

            当两棵树的当前节点都为 null 时返回 true

            当其中一个为 null 另一个不为 null 时返回 false

            当两个都不为空但是值不相等时，返回 false

            执行过程：当满足终止条件时进行返回，不满足时分别判断左子树和右子树是否相同，其中要注意代码中的短路效应

            时间复杂度：O(n)O(n)O(n)，nnn 为树的节点个数
        """
        if p is None or q is None:
            return p == q
        
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
# @lc code=end

