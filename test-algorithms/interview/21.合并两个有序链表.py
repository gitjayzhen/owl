#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#
# https://leetcode.cn/problems/merge-two-sorted-lists/description/
#
# test-algorithms
# Easy (66.74%)
# Likes:    2568
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 
# 
# 示例 2：
# 
# 
# 输入：l1 = [], l2 = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 两个链表的节点数目范围是 [0, 50]
# -100 
# l1 和 l2 均按 非递减顺序 排列
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
    def mergeTwoLists(self, list1, list2):
        """
        是一个纯逻辑的题目
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = head = ListNode()
        while list1 and list2:
            if list1.val >= list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next
        if list1:
            head.next = list1
        if list2:
            head.next = list2
        return result.next

            
# @lc code=end

