#
# @lc app=leetcode.cn id=83 lang=python
#
# [83] 删除排序链表中的重复元素
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (53.27%)
# Likes:    955
# Dislikes: 0
# Total Accepted:    551K
# Total Submissions: 1M
# Testcase Example:  '[1,1,2]'
#
# 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,1,2]
# 输出：[1,2]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1,1,2,3,3]
# 输出：[1,2,3]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列
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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        result = tmp = ListNode(head.val)
        while head.next:
            n = ListNode(head.next.val)
            if n.val != tmp.val:
                tmp.next = n
                tmp = n
            head = head.next
        return result
        
        
# @lc code=end

