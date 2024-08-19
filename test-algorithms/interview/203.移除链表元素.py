#
# @lc app=leetcode.cn id=203 lang=python
#
# [203] 移除链表元素
#
# https://leetcode.cn/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (56.10%)
# Likes:    1420
# Dislikes: 0
# Total Accepted:    732.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# 给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,6,3,4,5,6], val = 6
# 输出：[1,2,3,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [], val = 1
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [7,7,7,7], val = 7
# 输出：[]
# 
# 
# 
# 
# 提示：
# 
# 
# 列表中的节点数目在范围 [0, 10^4] 内
# 1 
# 0 
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        n_head = ListNode(-1, head)
        tmp = n_head
        while tmp.next:
            if tmp.next.val == val:
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        return n_head.next
# @lc code=end

