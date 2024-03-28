#
# @lc app=leetcode.cn id=2 lang=python
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        result = head = ListNode(0)
        mod_val = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            tmp = v1 + v2 + mod_val
            mod_val = tmp // 10
            head.next = ListNode(tmp % 10)
            head = head.next
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next
        if mod_val > 0:
            head.next = ListNode(mod_val)
        
        return result.next
        
# @lc code=end

