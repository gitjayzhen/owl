#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#
# https://leetcode.cn/problems/path-sum/description/
#
# algorithms
# Easy (54.03%)
# Likes:    1321
# Dislikes: 0
# Total Accepted:    643.7K
# Total Submissions: 1.2M
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点
# 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
# 
# 叶子节点 是指没有子节点的节点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# 输出：true
# 解释：等于目标和的根节点到叶节点路径如上图所示。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,2,3], targetSum = 5
# 输出：false
# 解释：树中存在两条根节点到叶子节点的路径：
# (1 --> 2): 和为 3
# (1 --> 3): 和为 4
# 不存在 sum = 5 的根节点到叶子节点的路径。
# 
# 示例 3：
# 
# 
# 输入：root = [], targetSum = 0
# 输出：false
# 解释：由于树是空的，所以不存在根节点到叶子节点的路径。
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [0, 5000] 内
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000
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
import collections


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        
        第一要素：明确函数作用
        第二要素：递归结束条件
        第三要素：函数等价关系
                
        1. 使用深度优先搜索（DFS），判断到叶子结点的时候，是不是 sum = targetSum
            - 终止条件：子节点的值等于最后的差值就是找到了，没有就是没有找到
            - 推进条件： 总值减去每个节点的值，左右分支都进入计算
            - 返回值：
            
        2. 使用 BFS 的方式来进行遍历
        """
        if root is None:
            return False
        # if not root.left and not root.right:
        #     return targetSum == root.val
        
        # return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        que = collections.deque()
        que.append((root, root.val))
        while que:
            root, path_sum = que.popleft()
            if not root.left and not root.right and path_sum == targetSum:
                return True
            if root.left:
                que.append((root.left, root.left.val + path_sum))
            if root.right:
                que.append((root.right, root.right.val + path_sum))
        return False
        
        
# @lc code=end

